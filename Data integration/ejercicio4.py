import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    """
    Encuentra los managers que tienen al menos cinco empleados directos.

    Parámetros:
    - employee (pd.DataFrame): DataFrame con columnas ['id', 'name', 'department', 'managerId']

    Retorna:
    - pd.DataFrame con una columna ['name'] que contiene los nombres de los managers con 5 o más reportes directos.
    """
    # Contar cuántos empleados reportan a cada managerId
    counts = employee.groupby('managerId').size().reset_index(name='direct_reports')
    
    # Filtrar managers con al menos 5 reportes y managerId no nulo
    filtered = counts[(counts['managerId'].notnull()) & (counts['direct_reports'] >= 5)]
    
    # Obtener el nombre del manager uniendo con la tabla employee (id == managerId)
    result = filtered.merge(employee, left_on='managerId', right_on='id')
    
    # Retornar solo la columna 'name'
    return result[['name']]

# Test local para probar la función
if __name__ == "__main__":
    data = {
        'id': [101, 102, 103, 104, 105, 106],
        'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron'],
        'department': ['A', 'A', 'A', 'A', 'A', 'B'],
        'managerId': [None, 101, 101, 101, 101, 101]
    }
    df = pd.DataFrame(data)
    print(find_managers(df))
