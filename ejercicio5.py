import pandas as pd


data = {
    'tweet_id': [1, 2, 3, 4],
    'content': [
        "short tweet",
        "this tweet is too long and invalid",
        "another one",
        "1234567890123456" 
    ]
}
tweets = pd.DataFrame(data)

# Función para obtener tweets inválidos
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets['content'].str.len() > 15][['tweet_id']]

# Ejecutar y mostrar resultado
print(invalid_tweets(tweets))
