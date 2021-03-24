import os
from glob import glob
import pandas as pd 
from giturlparse import parse
from time import time
from github import  Github,RateLimitExceededException
import github
import time
from time import sleep
import calendar

ACCESS_TOKEN = '6e9d18c39a5574590a7b1ec6b780ac3167f835fc'
 
g = Github(ACCESS_TOKEN)

def json_to_csv(filename=None,lines=None):
    
    if lines==None and filename!=None:
        with open(filename,'r') as f:
            lines = list(set(f.readlines()))


    csv_dict = {
        "name":[],
        "repo":[],
        "owner":[],
        #"user":[],
        "link":[],
        "stars":[]
    }

    for i in lines:
        data = parse(i)
        csv_dict["name"].append(data.name)
        csv_dict["repo"].append(data.repo)
        csv_dict["owner"].append(data.owner)
        #csv_dict["user"].append(data.user)
        csv_dict["link"].append(i)
        csv_dict["stars"].append(data.stars)

    print(csv_dict)

    df = pd.DataFrame(data=csv_dict)
    os.chdir("./csv/")
    filename = str(time())+str(".csv")
    open(filename,'w+').close()
    df.to_csv(filename)


def single_csv(filename=None,lines=None,owner=None):
    
    if lines==None and filename!=None:
        with open(filename,'r') as f:
            lines = list(set(f.readlines()))
    
   
    print(len(lines))    


    csv_dict = {
        "stars":[]
    }

    for i,j in zip(owner,lines):
        try:
            print(i,"/",j)
            data = g.get_repo(i+"/"+j)
            csv_dict["stars"].append(data.stargazers_count)
            print(data.stargazers_count)
        except StopIteration:
            break  # loop end
        except RateLimitExceededException:
            search_rate_limit = g.get_rate_limit().search
            print('search remaining: {}'.format(search_rate_limit.remaining))
            reset_timestamp = calendar.timegm(search_rate_limit.reset.timetuple())
                    # add 10 seconds to be sure the rate limit has been reset
            sleep_time = reset_timestamp - calendar.timegm(time.gmtime()) + 10
            time.sleep(sleep_time)
            continue  
        except Exception:
            continue  

    print(csv_dict)

    df = pd.DataFrame(data=csv_dict)
    return df

if __name__=="__main__":
    df = pd.read_csv('./final.csv')
    df_star = single_csv(lines=list(df["repo"]),owner=list(df["owner"]))
    df["star"] = df_star
    df.to_csv("./mod.csv")