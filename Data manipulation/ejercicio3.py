import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    """
    Encuentra empleados con el salario más alto en cada departamento, y devuelve un DataFrame con:
    Department (nombre del departamento), Employee (nombre del empleado), Salary (salario).
    """

    # 1. Obtener salario máximo por departamento
    max_salary_per_dept = employee.groupby('departmentId')['salary'].max().reset_index()

    # 2. Filtrar empleados que tienen el salario máximo en su departamento
    top_earners = pd.merge(employee, max_salary_per_dept, 
                           how='inner',
                           left_on=['departmentId', 'salary'],
                           right_on=['departmentId', 'salary'])

    # 3. Unir con tabla Department para obtener el nombre del departamento
    merged = pd.merge(top_earners, department, left_on='departmentId', right_on='id', suffixes=('', '_dept'))

    # 4. Seleccionar y renombrar columnas para que coincida con la salida esperada
    result = merged[['name_dept', 'name', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']

    return result

# --- Código para prueba ---

if __name__ == "__main__":
    employee_df = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
        'salary': [70000, 90000, 80000, 60000, 90000],
        'departmentId': [1, 1, 2, 2, 1]
    })

    department_df = pd.DataFrame({
        'id': [1, 2],
        'name': ['IT', 'Sales']
    })

    print(department_highest_salary(employee_df, department_df))
