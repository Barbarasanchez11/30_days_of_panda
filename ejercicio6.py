import pandas as pd


data = {
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Michael', 'John', 'Maria', 'David'],
    'salary': [50000, 60000, 55000, 70000, 45000]
}

employees = pd.DataFrame(data)


def calculate_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Crear una nueva columna 'bonus' inicializada en 0
    employees['bonus'] = 0

    # Condición: ID impar y nombre que no empiece con 'M'
    condition = (employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M'))

    # Aplicar la condición
    employees.loc[condition, 'bonus'] = employees['salary']

    # Devolver solo las columnas requeridas, ordenado
    return employees[['employee_id', 'bonus']].sort_values('employee_id').reset_index(drop=True)

# Ejecutar en VSCode
if __name__ == "__main__":
    result = calculate_bonus(employees)
    print(result)
