

import pandas as pd

# read csv files
df_users = pd.read_csv('Data/Users.csv', dtype=str)
df_ratings = pd.read_csv('Data/Ratings.csv', dtype=str)
df_books = pd.read_csv('Data/Books.csv', dtype=str)

# drop any users where a column is missing
df_users.dropna(subset=['User-ID', 'Location', 'Age'], inplace=True)
# drop any users whcih have been removed
df_ratings = df_ratings[df_ratings['User-ID'].isin(df_users['User-ID'])]
# drop any book which has been removed from ratings
df_books = df_books[df_books['ISBN'].isin(df_ratings['ISBN'])]

# drop where ratings equal 0
df_ratings = df_ratings[df_ratings['Book-Rating'] != '0']
# remove any users who have no ratings
df_users = df_users[df_users['User-ID'].isin(df_ratings['User-ID'])]
# remove any books which have no ratings
df_books = df_books[df_books['ISBN'].isin(df_ratings['ISBN'])]

merged = pd.merge(df_users, df_ratings, on='User-ID', how='inner')
merged = pd.merge(merged, df_books, on='ISBN', how='inner')
merged.drop('Image-URL-S', axis=1, inplace=True)
merged.drop('Image-URL-M', axis=1, inplace=True)
merged.drop('Image-URL-L', axis=1, inplace=True)

def has_complete_location(location):
    components = location.split(',')
    return len(components) >= 3 and all(components[:3])

merged = merged[merged['Location'].apply(has_complete_location)]

location = merged['Location'].str.split(', ', expand=True)

merged['City'] = location[0]
merged['State'] = location[1]
merged['Country'] = location[2]

merged.drop(columns=['Location'], inplace=True)

# return new reduced dataframes to csv files
df_users.to_csv('Data/Users_Reduced.csv', index=False)
df_ratings.to_csv('Data/Ratings_Reduced.csv', index=False)
df_books.to_csv('Data/Books_Reduced.csv', index=False)
merged.to_csv('Data/Merged.csv', index=False)