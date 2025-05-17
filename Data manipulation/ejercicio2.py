import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    """
    Función para encontrar el segundo salario más alto distinto en un DataFrame de empleados.

    Parámetros:
    - employee: pd.DataFrame con columnas 'id' y 'salary'

    Retorna:
    - pd.DataFrame con una sola fila y columna 'SecondHighestSalary' que contiene
      el segundo salario más alto distinto, o None si no existe.
    """

    # 1. Obtener los salarios distintos para no contar duplicados
    distinct_salaries = employee['salary'].drop_duplicates()

    # 2. Ordenar los salarios de mayor a menor para identificar fácilmente el segundo más alto
    distinct_salaries = distinct_salaries.sort_values(ascending=False)

    # 3. Verificar que haya al menos dos salarios distintos
    if len(distinct_salaries) >= 2:
        # Si sí, tomar el segundo salario (índice 1)
        second_highest = distinct_salaries.iloc[1]
    else:
        # Si no, asignar None para indicar que no hay segundo salario distinto
        second_highest = None

    # 4. Crear un DataFrame con el resultado, con la columna nombrada correctamente
    result_df = pd.DataFrame({'SecondHighestSalary': [second_highest]})

    return result_df


# --- Código de prueba ---

if __name__ == "__main__":
    # Crear un DataFrame de ejemplo con empleados y sus salarios
    df = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'salary': [100, 200, 200, 300]
    })

    # Llamar a la función y mostrar el resultado
    print(second_highest_salary(df))
