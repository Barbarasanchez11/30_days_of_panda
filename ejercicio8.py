import pandas as pd


data = {
    'user_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'mail': ['alice_123@leetcode.com', 'bob123@leetcode.com', 'charlie@google.com', 'david@leetcode.com']
}

users = pd.DataFrame(data)


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
 
    valid_condition = (
        users['mail'].str.endswith('@leetcode.com') & 
        users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9._-]*@') 
    )
    

    valid_users = users[valid_condition]

    return valid_users[['user_id', 'name', 'mail']] 


if __name__ == "__main__":
    result = valid_emails(users)
    print(result)
