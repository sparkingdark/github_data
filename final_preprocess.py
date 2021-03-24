import  pandas as pd

author = '/home/debo/Downloads/Some spreadsheet GitHub projects - Computer vision (1).csv'
result = '/home/debo/Downloads/result (3).csv'

df1 = pd.read_csv(author)
df2 = pd.read_csv(result)

df1['email'] = df2['email']

df1.to_csv('./final.csv')