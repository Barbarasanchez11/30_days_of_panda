import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    """
    Encuentra la primera fecha de login para cada jugador.
    
    Parámetros:
    activity (pd.DataFrame): DataFrame con columnas:
        - 'player_id': ID del jugador
        - 'device_id': ID del dispositivo usado
        - 'event_date': fecha del evento (login)
        - 'games_played': cantidad de juegos jugados en esa sesión
    
    Retorna:
    pd.DataFrame: DataFrame con columnas:
        - 'player_id': ID del jugador
        - 'first_login': la fecha del primer login del jugador
    """

    # Agrupar por 'player_id' y obtener la fecha mínima 'event_date' (primer login)
    first_login = activity.groupby('player_id', as_index=False)['event_date'].min()
    
    # Renombrar la columna 'event_date' a 'first_login' para que coincida con la salida esperada
    first_login.rename(columns={'event_date': 'first_login'}, inplace=True)
    
    return first_login


# Ejemplo para probar la función localmente
if __name__ == "__main__":
    data = {
        'player_id': [1, 1, 2, 3, 3],
        'device_id': [2, 2, 3, 1, 4],
        'event_date': ['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03'],
        'games_played': [5, 6, 1, 0, 5]
    }
    df = pd.DataFrame(data)
    
    # Convertir 'event_date' a tipo fecha para mayor precisión en operaciones de fecha
    df['event_date'] = pd.to_datetime(df['event_date'])
    
    result = game_analysis(df)
    print(result)
