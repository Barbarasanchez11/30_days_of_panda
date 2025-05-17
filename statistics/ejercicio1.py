import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    """
    Cuenta cuántas cuentas bancarias hay en cada categoría salarial:
    'Low Salary', 'Average Salary' y 'High Salary'.
    """

    # 1. Clasificamos cada ingreso en su categoría
    conditions = pd.cut(
        accounts['income'],
        bins=[-float('inf'), 20000, 50000, float('inf')],  # rangos
        labels=['Low Salary', 'Average Salary', 'High Salary'],  # nombres
        right=False  # el límite superior NO está incluido (para cumplir "<" y ">")
    )

    # 2. Contamos cuántas cuentas hay por categoría
    salary_counts = conditions.value_counts().reindex(
        ['Low Salary', 'Average Salary', 'High Salary'], fill_value=0
    ).reset_index()

    # 3. Renombramos las columnas para el resultado final
    salary_counts.columns = ['category', 'accounts_count']

    return salary_counts


# Ejemplo para probar localmente en VSCode
if __name__ == "__main__":
    df = pd.DataFrame({
        'account_id': [1, 2, 3, 4, 5, 6],
        'income': [10000, 25000, 50000, 70000, 15000, 51000]
    })

    result = count_salary_categories(df)
    print(result)
