import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Obtener los IDs de las compañías con nombre "RED"
    red_company_ids = company.loc[company['name'] == 'RED', 'com_id']
    
    # Filtrar las órdenes que pertenecen a la compañía "RED"
    red_orders = orders[orders['com_id'].isin(red_company_ids)]
    
    # Obtener los IDs de vendedores que han realizado órdenes con la compañía "RED"
    sales_with_red_orders = red_orders['sales_id'].unique()
    
    # Filtrar vendedores que NO han realizado órdenes con la compañía "RED"
    sales_without_red_orders = sales_person[~sales_person['sales_id'].isin(sales_with_red_orders)]
    
    # Retornar solo los nombres de esos vendedores
    return sales_without_red_orders[['name']]


if __name__ == "__main__":
    # Ejemplo para test local
    sales_person_data = {
        'sales_id': [1, 2, 3, 4],
        'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'salary': [5000, 6000, 5500, 6200],
        'commission_rate': [5, 7, 6, 5],
        'hire_date': ['2020-01-01', '2019-06-15', '2021-03-20', '2018-12-01']
    }
    company_data = {
        'com_id': [101, 102],
        'name': ['RED', 'BLUE'],
        'city': ['New York', 'San Francisco']
    }
    orders_data = {
        'order_id': [1001, 1002, 1003, 1004],
        'order_date': ['2023-01-10', '2023-01-15', '2023-01-20', '2023-01-25'],
        'com_id': [101, 102, 101, 102],
        'sales_id': [1, 2, 3, 4],
        'amount': [500, 700, 300, 400]
    }

    sales_person_df = pd.DataFrame(sales_person_data)
    company_df = pd.DataFrame(company_data)
    orders_df = pd.DataFrame(orders_data)

    result = sales_person(sales_person_df, company_df, orders_df)
    print(result)
