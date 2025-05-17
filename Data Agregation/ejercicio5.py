import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Encuentra el customer_number del cliente con mayor cantidad de pedidos.

    Parámetros:
    orders (pd.DataFrame): DataFrame con columnas 'order_number' y 'customer_number'.

    Retorna:
    pd.DataFrame: DataFrame con una sola fila y columna 'customer_number' del cliente con más pedidos.
    """
    
    # Contar la cantidad de pedidos por cliente
    order_counts = orders.groupby('customer_number').size().reset_index(name='order_count')
    
    # Encontrar el máximo número de pedidos
    max_orders = order_counts['order_count'].max()
    
    # Filtrar el cliente con la mayor cantidad de pedidos
    top_customer = order_counts[order_counts['order_count'] == max_orders]
    
    # Retornar solo la columna 'customer_number'
    return top_customer[['customer_number']]


# Ejemplo para probar localmente
if __name__ == "__main__":
    data = {
        'order_number': [1, 2, 3, 4, 5, 6, 7],
        'customer_number': [100, 101, 100, 102, 101, 100, 103]
    }
    df = pd.DataFrame(data)
    print(largest_orders(df))
