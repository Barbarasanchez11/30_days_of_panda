import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula la cantidad de materias únicas que enseña cada profesor.
    
    Parámetros:
    teacher (pd.DataFrame): DataFrame con columnas 'teacher_id', 'subject_id', 'dept_id'.
    
    Retorna:
    pd.DataFrame: DataFrame con columnas:
        - 'teacher_id': ID del profesor
        - 'cnt': número de materias únicas que enseña ese profesor
    """
    
    # Agrupar por 'teacher_id' y contar la cantidad de valores distintos en 'subject_id'
    unique_counts = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    
    # Renombrar la columna para que coincida con el nombre esperado por el sistema
    unique_counts.rename(columns={'subject_id': 'cnt'}, inplace=True)
    
    return unique_counts


# Ejemplo para probar la función localmente
if __name__ == "__main__":
    data = {
        'teacher_id': [1, 1, 2, 2, 3],
        'subject_id': [2, 2, 1, 2, 3],
        'dept_id': [3, 4, 1, 1, 1]
    }
    df = pd.DataFrame(data)
    
    result = count_unique_subjects(df)
    print(result)
