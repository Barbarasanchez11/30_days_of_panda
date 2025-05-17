import pandas as pd


data = {
    'name': ['China', 'India', 'USA', 'Monaco', 'Australia', 'Vatican City'],
    'continent': ['Asia', 'Asia', 'North America', 'Europe', 'Oceania', 'Europe'],
    'area': [9596961, 3287263, 9833517, 2, 7692024, 0.49],
    'population': [1400000000, 1353000000, 331000000, 39000, 25600000, 825],
    'gdp': [14342900000000, 2875140000000, 21433200000000, 7480000000, 1392687000000, 0]
}

world = pd.DataFrame(data)


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world['area'] >= 3000000) | (world['population'] >= 25000000)][['name', 'population', 'area']]


result = big_countries(world)
print(result)
