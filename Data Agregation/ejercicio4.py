import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    """
    Encuentra las clases que tienen al menos 5 estudiantes inscritos.
    
    Parámetros:
    courses (pd.DataFrame): DataFrame con columnas 'student' y 'class'.
    
    Retorna:
    pd.DataFrame: DataFrame con la columna 'class' que contiene las clases con al menos 5 estudiantes.
    """
    
    # Contar la cantidad de estudiantes por cada clase
    class_counts = courses.groupby('class')['student'].count().reset_index()
    
    # Filtrar solo las clases con 5 o más estudiantes
    classes_5_or_more = class_counts[class_counts['student'] >= 5]
    
    # Seleccionar solo la columna 'class' para la salida
    result = classes_5_or_more[['class']]
    
    return result


# Ejemplo para probar la función localmente
if __name__ == "__main__":
    data = {
        'student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
        'class': ['Math', 'Math', 'Math', 'Math', 'Math', 'History', 'History', 'History', 'History', 'Science']
    }
    df = pd.DataFrame(data)
    
    result = find_classes(df)
    print(result)
