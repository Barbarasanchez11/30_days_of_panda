import pandas as pd


data = {
    'user_id': [3, 1, 2],
    'name': ['aLIcE', 'JOHN', 'maria']
}


users = pd.DataFrame(data)

# Función que corrige los nombres
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # Capitaliza el nombre: primera letra mayúscula, el resto minúscula
    users['name'] = users['name'].str.capitalize()
    # Ordena por user_id
    return users.sort_values('user_id').reset_index(drop=True)

# Ejecutar y mostrar resultado
if __name__ == "__main__":
    result = fix_names(users)
    print(result)
