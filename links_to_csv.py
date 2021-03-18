import os
from glob import glob
import pandas as pd 
from giturlparse import parse
from time import time



def json_to_csv(filename):

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
    os.chdir("./csv/")
    filename = str(time())+str(".csv")
    open(filename,'w+').close()
    df.to_csv(filename)


def single_csv(dir_path):
    
    lines = None
    
    with open(dir_path,'r') as f:
        lines = list(set(f.readlines()))
    print(len(lines))    


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

    #print(csv_dict)

    df = pd.DataFrame(data=csv_dict)
    df.to_csv('./data.csv')


if __name__=="__main__":
    dir_path = 'links.txt'
    single_csv(dir_path)