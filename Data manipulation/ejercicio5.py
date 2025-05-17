import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    """
    Elimina duplicados en la columna 'email', dejando solo la fila con menor 'id' para cada email.
    Modifica el DataFrame 'person' in place.
    """
    # Ordena por 'id' ascendente para mantener la fila con menor id primero
    person.sort_values('id', inplace=True)
    # Elimina duplicados basándose en 'email', manteniendo la primera aparición (menor id)
    person.drop_duplicates(subset='email', keep='first', inplace=True)


if __name__ == "__main__":
    # DataFrame de ejemplo para pruebas locales
    person_df = pd.DataFrame({
        'id': [3, 1, 2, 4],
        'email': ['a@example.com', 'b@example.com', 'a@example.com', 'c@example.com']
    })

    print("Antes de eliminar duplicados:")
    print(person_df)

    # Llamamos a la función para modificar el DataFrame in place
    delete_duplicate_emails(person_df)

    print("\nDespués de eliminar duplicados:")
    print(person_df)
