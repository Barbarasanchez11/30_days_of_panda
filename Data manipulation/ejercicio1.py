import pandas as pd

# Definimos una función que toma como entrada:
# - employee: un DataFrame con las columnas 'id' y 'salary'
# - N: un entero que indica qué salario más alto queremos obtener
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    
    # 1. Eliminamos sueldos repetidos usando drop_duplicates()
    # 2. Ordenamos los sueldos de mayor a menor con sort_values(ascending=False)
    distinct_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # 3. Si hay suficientes sueldos distintos (N <= cantidad de sueldos únicos)
    if N <= len(distinct_salaries):
        # Accedemos al enésimo sueldo más alto (índice N-1 por índice base cero)
        result = distinct_salaries.iloc[N - 1]
    else:
        # Si no hay suficientes sueldos distintos, devolvemos None
        result = None

    # 4. Devolvemos el resultado como un DataFrame de una sola fila
    #    con la columna nombrada como 'getNthHighestSalary(N)' (ej: getNthHighestSalary(2))
    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})

df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'salary': [100, 200, 200, 300]
})

print(nth_highest_salary(df, 2))
