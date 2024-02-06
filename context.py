import pandas as pd

user_data = pd.read_csv('Data/Users_Reduced.csv', dtype=str)

def get_user_id():
    user_id = input('Enter User-ID, if new user enter "new"')
    new_user = False
    if user_id == 'new':
        new_user = True
    elif str(user_id) in user_data['User-ID'].values:
        print(f'Logged in with User-ID: {user_id}')
    else:
        print(f'No User-ID: {user_id} found, try again')
        return get_user_id()
    return str(user_id), new_user

def get_profile(user_id):
    return user_data[user_data['User-ID'] == user_id].values[0]



