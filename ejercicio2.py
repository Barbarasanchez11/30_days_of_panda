import pandas as pd


data = {
    'product_id': [1, 2, 3, 4, 5],
    'low_fats': ['Y', 'N', 'Y', 'Y', 'N'],
    'recyclable': ['Y', 'Y', 'N', 'Y', 'N']
}

products = pd.DataFrame(data)

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')][['product_id']]


result = find_products(products)
print(result)
