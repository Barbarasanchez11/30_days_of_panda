import pandas as pd


customers_data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max']
}
customers = pd.DataFrame(customers_data)


orders_data = {
    'id': [1, 2],
    'customerId': [3, 1]
}
orders = pd.DataFrame(orders_data)

# Función para encontrar clientes que nunca hicieron pedidos
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = customers[~customers['id'].isin(orders['customerId'])][['name']]
    result.columns = ['Customers']  
    return result


result_df = find_customers(customers, orders)
print(result_df)
