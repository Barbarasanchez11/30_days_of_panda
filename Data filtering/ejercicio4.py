import pandas as pd


data = {
    'article_id': [1, 1, 2, 2, 3],
    'author_id': [1, 1, 2, 2, 3],
    'viewer_id': [1, 3, 2, 4, 3],
    'view_date': ['2024-07-01', '2024-07-01', '2024-07-01', '2024-07-01', '2024-07-01']
}

views = pd.DataFrame(data)

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    filtered = views[views['author_id'] == views['viewer_id']]
    result = filtered[['author_id']].drop_duplicates().rename(columns={'author_id': 'id'})
    return result.sort_values('id').reset_index(drop=True)


print(article_views(views))
