import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    """
    Dadas dos tablas:

    - employees: con columnas 'id' (identificador del empleado) y 'name' (nombre del empleado).
    - employee_uni: con columnas 'id' y 'unique_id' (identificador único asignado a algunos empleados).

    Se desea obtener la lista de empleados con su 'unique_id' correspondiente. 

    Si un empleado no tiene un 'unique_id' asociado en la tabla employee_uni, debe aparecer con valor NULL (NaN en pandas).

    Se debe retornar un DataFrame con las columnas ['unique_id', 'name'].

    Parámetros:
    - employees (pd.DataFrame): DataFrame con columnas ['id', 'name'].
    - employee_uni (pd.DataFrame): DataFrame con columnas ['id', 'unique_id'].

    Retorna:
    - pd.DataFrame con columnas ['unique_id', 'name'], donde 'unique_id' es el identificador único si existe, o NULL en caso contrario.
    """
    # Merge left para mantener todos los empleados
    merged = pd.merge(employees, employee_uni, on='id', how='left')
    
    # Seleccionamos solo las columnas necesarias en el orden requerido
    result = merged[['unique_id', 'name']]
    
    return result

# Ejemplo para test local
if __name__ == "__main__":
    employees_data = {
        'id': [1, 7, 11, 90, 3],
        'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
    }
    employee_uni_data = {
        'id': [3, 11, 90],
        'unique_id': [1, 2, 3]
    }
    employees_df = pd.DataFrame(employees_data)
    employee_uni_df = pd.DataFrame(employee_uni_data)
    
    print(replace_employee_id(employees_df, employee_uni_df))
