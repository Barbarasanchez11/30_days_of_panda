import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    """
    Esta función recibe un DataFrame con datos de ventas diarias y para cada combinación
    de fecha y producto calcula:
      - La cantidad de leads únicos (clientes potenciales)
      - La cantidad de partners únicos

    Explicación importante:
    En el método `groupby.agg()`, usamos `pd.NamedAgg` para:
      - Especificar el nombre que queremos para la nueva columna resultante (por ejemplo, 'unique_leads')
      - Indicar qué columna del DataFrame vamos a agregar ('lead_id' o 'partner_id')
      - Definir qué función de agregación usar (aquí `nunique` para contar valores únicos)

    En resumen, `pd.NamedAgg(column='lead_id', aggfunc='nunique')` significa:
      "Cuenta los valores únicos en la columna 'lead_id' y llama a esta nueva columna 'unique_leads'"

    Parámetros:
      daily_sales (pd.DataFrame): DataFrame con columnas 'date_id', 'make_name', 'lead_id', 'partner_id'.

    Retorna:
      pd.DataFrame con columnas:
        - 'date_id'
        - 'make_name'
        - 'unique_leads' (conteo de leads únicos)
        - 'unique_partners' (conteo de partners únicos)
    """
    grouped = daily_sales.groupby(['date_id', 'make_name']).agg(
        unique_leads=pd.NamedAgg(column='lead_id', aggfunc='nunique'),    # Cuenta leads únicos y nombra la columna 'unique_leads'
        unique_partners=pd.NamedAgg(column='partner_id', aggfunc='nunique') # Cuenta partners únicos y nombra la columna 'unique_partners'
    ).reset_index()

    return grouped


if __name__ == "__main__":
    # Datos de ejemplo para pruebas locales
    data = {
        'date_id': ['2020-12-08', '2020-12-08', '2020-12-08', '2020-12-07', '2020-12-07', '2020-12-08'],
        'make_name': ['toyota', 'toyota', 'toyota', 'toyota', 'toyota', 'honda'],
        'lead_id': [0, 1, 1, 0, 0, 1],
        'partner_id': [1, 0, 2, 2, 1, 2]
    }
    df = pd.DataFrame(data)
    df['date_id'] = pd.to_datetime(df['date_id'])

    print(daily_leads_and_partners(df))
