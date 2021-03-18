from github import Github
import time
from time import sleep
import calendar
 
ACCESS_TOKEN = '6e9d18c39a5574590a7b1ec6b780ac3167f835fc'
 
g = Github(ACCESS_TOKEN)
 
 
def search_github(keywords,filename):
    query = '+'.join(keywords) + '+in:readme+in:description'
   

    from github import RateLimitExceededException
    count = 0
    result = g.search_repositories(query, 'stars', 'desc')
    iter_obj = iter(result)
    while True:
        try:
            repo  = next(iter_obj)
            with open(filename, 'a+') as f:
                f.write(repo.clone_url + '\n')
                count += 1
                #logger.info(count)
                print(count)
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
 
    #print(f'Found {result.totalCount} repo(s)')
 
    # for repo in result:
    #     print(f'{repo.clone_url}, {repo.stargazers_count} stars')
 

def keyword_list(keywords=list()):
    keyword_splitter = lambda keyword:[keyword.strip() for keyword in keyword.split(',')]
    all_splitted_text = []
    if len(keywords)!=0:
        for word_list in keywords:
            all_splitted_text.append(keyword_splitter(word_list))
    return all_splitted_text

# def write_to_txt(keywords):
#     result = search_github(keywords)
#     filename = "".join(keywords)+".txt"
#     with open(filename,'w+') as f:
#         for repo in result:
#             if repo.stargazers_count>60:
#                 f.writelines(repo.clone_url+"\n")
#                 print("done")    

if __name__=="__main__":
    #all_keywords = ["awesome,deep learning","awesome,machine learning","awesome,python","awesome,computer vision","awesome,nlp","awesome,supervised learning","awesome,RL",'awesome,Reinforcement learning']
    all_keywords = ["computer vision,python","computer vision,projects",]
    all_text = keyword_list(all_keywords)

    print(all_text)

    for i in all_text:
        search_github(i,"links.txt")