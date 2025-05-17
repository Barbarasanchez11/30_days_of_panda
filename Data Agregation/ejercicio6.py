import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    """
    Para cada fecha, encuentra el número de productos diferentes vendidos y sus nombres ordenados alfabéticamente.
    
    Parámetros:
    activities (pd.DataFrame): DataFrame con columnas 'sell_date' y 'product'.
    
    Retorna:
    pd.DataFrame: DataFrame con columnas:
        - 'sell_date': fecha de venta
        - 'num_sold': número de productos únicos vendidos en esa fecha
        - 'products': nombres de productos vendidos ese día, ordenados y separados por comas
    """
    # Agrupar por 'sell_date' y obtener la lista ordenada de productos únicos
    grouped = activities.groupby('sell_date')['product'].apply(lambda x: sorted(set(x))).reset_index()
    
    # Calcular el número de productos únicos vendidos en cada fecha
    grouped['num_sold'] = grouped['product'].apply(len)
    
    # Convertir la lista de productos a un string separado por comas
    grouped['products'] = grouped['product'].apply(lambda x: ','.join(x))
    
    # Seleccionar solo las columnas necesarias para el resultado
    result = grouped[['sell_date', 'num_sold', 'products']]
    
    # Ordenar el resultado por fecha de venta
    result = result.sort_values('sell_date').reset_index(drop=True)
    
    return result

# Ejemplo para probar la función localmente
if __name__ == "__main__":
    data = {
        'sell_date': ['2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30', '2020-06-01', '2020-06-02'],
        'product': ['Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'Mask']
    }
    df = pd.DataFrame(data)
    df['sell_date'] = pd.to_datetime(df['sell_date'])
    
    print(categorize_products(df))
