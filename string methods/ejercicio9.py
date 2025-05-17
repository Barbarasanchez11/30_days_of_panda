import pandas as pd


data = {
    'patient_id': [1, 2, 3, 4, 5],
    'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'],
    'conditions': ['YFEV COUGH', '', 'DIAB100 MYOP', 'ACNE DIAB100', 'DIAB201']
}

patients = pd.DataFrame(data)

# Asegurarse de que la columna 'conditions' no tiene valores nulos y es tipo string
patients['conditions'] = patients['conditions'].fillna('').astype(str)

# Función para encontrar pacientes con Type I Diabetes (DIAB1)
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Condición: "DIAB1" debe aparecer en alguna parte de las condiciones
    condition = patients['conditions'].str.contains(r'(?<!\+)\bDIAB1\d+\b', case=False, na=False)
    
    # Filtrar pacientes que cumplen la condición
    diabetes_patients = patients[condition]

    # Devolver las columnas requeridas
    return diabetes_patients[['patient_id', 'patient_name', 'conditions']]

# Ejecutar y mostrar los pacientes con Type I Diabetes
if __name__ == "__main__":
    result = find_patients(patients)
    print(result)
