import pandas as pd 
from giturlparse import parse
import os


def json_to_csv(filename,root_name):

    lines = None
    
    with open(filename,'r') as f:
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
    open("./csv/"+root_name+str(".csv"),'w+').close()
    df.to_csv("./csv/"+root_name)


if __name__=="__main__":
    for filename in os.listdir("./links/"):
        root_name = os.path.splitext(filename)[0]
        json_to_csv(os.path.join("./links/",filename),root_name)