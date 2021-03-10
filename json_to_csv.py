import pandas as pd 
from giturlparse import parse



lines = None

with open('links.txt','r') as f:
    lines = list(set(f.readlines()))


csv_dict = {
    "name":[],
    "repo":[],
    "owner":[],
    #"user":[],
    "link":[]
}

for i in lines:
    data = parse(i)
    csv_dict["name"].append(data.name)
    csv_dict["repo"].append(data.repo)
    csv_dict["owner"].append(data.owner)
    #csv_dict["user"].append(data.user)
    csv_dict["link"].append(i)

print(csv_dict)

df = pd.DataFrame(data=csv_dict)

df.to_csv('./data.csv')