import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma la tabla de productos de formato ancho a formato largo:
    De (product_id, store1, store2, store3) a (product_id, store, price),
    excluyendo filas donde price es null.
    """

    # 1. Hacer melt para "derretir" las columnas de tiendas en una columna 'store'
    melted = products.melt(id_vars='product_id', 
                           value_vars=['store1', 'store2', 'store3'],
                           var_name='store', 
                           value_name='price')

    # 2. Filtrar filas donde price NO sea null (producto disponible en esa tienda)
    melted = melted[melted['price'].notnull()]

    # 3. Opcional: si quieres, quitar el prefijo "store" para que quede solo "1", "2", "3"
    # melted['store'] = melted['store'].str.replace('store', '')

    # 4. Resetear índice para orden limpio
    melted = melted.reset_index(drop=True)

    return melted

if __name__ == "__main__":
    products_df = pd.DataFrame({
        'product_id': [101, 102, 103],
        'store1': [10.0, None, 15.0],
        'store2': [12.0, 13.0, None],
        'store3': [None, 14.0, 16.0]
    })

    print(rearrange_products_table(products_df))

