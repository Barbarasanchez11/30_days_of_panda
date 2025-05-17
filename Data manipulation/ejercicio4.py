import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el ranking de los scores según las reglas dadas:
    - ranking descendente (mayor score = 1)
    - empates con el mismo ranking
    - rankings consecutivos sin huecos (método 'dense')
    
    Parámetros:
    - scores: DataFrame con columnas ['id', 'score']
    
    Retorna:
    - DataFrame con columnas ['score', 'rank'], ordenado por score descendente
    """

    # 1. Ordenar scores de mayor a menor para luego calcular ranking
    scores_sorted = scores.sort_values(by='score', ascending=False).copy()

    # 2. Calcular el ranking usando método 'dense' para evitar huecos en rankings
    scores_sorted['rank'] = scores_sorted['score'].rank(method='dense', ascending=False).astype(int)

    # 3. Seleccionar columnas requeridas (si quieres puedes mantener 'id' también)
    result = scores_sorted[['score', 'rank']]

    # 4. Devolver resultado ordenado por score descendente (ya está ordenado pero por seguridad)
    return result.reset_index(drop=True)


# --- Código para probar la función ---

if __name__ == "__main__":
    df = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'score': [100.00, 100.00, 90.00, 80.00, 80.00]
    })

    print(order_scores(df))
