import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # Producto cartesiano para obtener todas las combinaciones de student_id y subject_name
    full_combo = students.assign(key=1).merge(subjects.assign(key=1), on='key').drop('key', axis=1)

    # Contar cuántas veces cada estudiante asistió a cada examen
    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

    # Hacer merge para unir todas las combinaciones con los conteos de exámenes
    result = full_combo.merge(exam_counts, on=['student_id', 'subject_name'], how='left')

    # Reemplazar valores NaN (donde no hay registros) por 0 y convertir a entero
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)

    # Ordenar resultado por student_id y subject_name
    return result.sort_values(['student_id', 'subject_name']).reset_index(drop=True)

# Ejemplo de prueba para correr localmente
if __name__ == "__main__":
    students = pd.DataFrame({
        'student_id': [1, 2, 13, 6],
        'student_name': ['Alice', 'Bob', 'John', 'Alex']
    })
    subjects = pd.DataFrame({
        'subject_name': ['Math', 'Physics', 'Programming']
    })
    examinations = pd.DataFrame({
        'student_id': [1, 1, 1, 2, 1, 1],
        'subject_name': ['Math', 'Physics', 'Programming', 'Programming', 'Physics', 'Math']
    })

    print(students_and_examinations(students, subjects, examinations))
