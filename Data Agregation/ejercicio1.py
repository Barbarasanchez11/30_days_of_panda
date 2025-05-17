import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el tiempo total en minutos que cada empleado pasó en la oficina por cada día.
    
    Parámetros:
    employees (pd.DataFrame): DataFrame con columnas 'emp_id', 'event_day', 'in_time', 'out_time'.
    
    Retorna:
    pd.DataFrame: DataFrame con columnas 'day', 'emp_id', 'total_time' donde:
        - 'day' es la fecha del evento,
        - 'emp_id' es el ID del empleado,
        - 'total_time' es la suma de minutos que el empleado estuvo en la oficina ese día.
    """
    
    # Crear una nueva columna 'session_time' con la duración de cada sesión (out_time - in_time)
    employees['session_time'] = employees['out_time'] - employees['in_time']
    
    # Agrupar por empleado y día, sumando el tiempo total de todas las sesiones en ese día
    result = employees.groupby(['emp_id', 'event_day'], as_index=False)['session_time'].sum()
    
    # Renombrar las columnas para que coincidan con el formato esperado de salida
    result.rename(columns={'session_time': 'total_time', 'event_day': 'day'}, inplace=True)
    
    # Reordenar las columnas para que la primera sea 'day', luego 'emp_id' y finalmente 'total_time'
    result = result[['day', 'emp_id', 'total_time']]
    
    return result

# Ejemplo rápido para probar la función:
if __name__ == "__main__":
    # Crear un DataFrame de ejemplo con los datos dados
    data = {
        'emp_id': [1, 1, 1, 2, 2],
        'event_day': ['2020-11-28', '2020-11-28', '2020-12-03', '2020-11-28', '2020-12-09'],
        'in_time': [4, 55, 1, 3, 47],
        'out_time': [32, 200, 42, 33, 74]
    }
    df = pd.DataFrame(data)
    
    # Ejecutar la función y mostrar el resultado
    output = total_time(df)
    print(output)
