import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    """
    Dado un DataFrame con columnas:
      - actor_id
      - director_id
      - timestamp (único por fila)

    Queremos encontrar todos los pares (actor_id, director_id) donde el actor ha
    trabajado con ese director al menos 3 veces.

    Pasos:
      1. Agrupar por actor_id y director_id.
      2. Contar cuántas filas (cooperaciones) hay por cada par.
      3. Filtrar para quedarnos solo con los pares donde la cuenta es >= 3.
      4. Devolver un DataFrame con las columnas actor_id y director_id que cumplen la condición.
    """
    # Agrupamos por actor y director y contamos las filas
    counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='cooperation_count')
    
    # Filtramos solo los pares con al menos 3 cooperaciones
    filtered = counts[counts['cooperation_count'] >= 3]
    
    # Seleccionamos solo las columnas requeridas para la salida
    result = filtered[['actor_id', 'director_id']]
    
    return result


if __name__ == "__main__":
    # Ejemplo simple para probar
    data = {
        'actor_id': [1, 1, 1, 2, 2, 3, 1, 1],
        'director_id': [10, 10, 10, 20, 20, 30, 10, 40],
        'timestamp': [1, 2, 3, 4, 5, 6, 7, 8]
    }
    df = pd.DataFrame(data)
    
    print(actors_and_directors(df))
