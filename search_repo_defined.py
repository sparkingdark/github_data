from github import Github
from time import sleep
 
ACCESS_TOKEN = '6e9d18c39a5574590a7b1ec6b780ac3167f835fc'
 
g = Github(ACCESS_TOKEN)
 
 
def search_github(keywords):
    query = '+'.join(keywords) + '+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')
 
    #print(f'Found {result.totalCount} repo(s)')

    return result
 
    # for repo in result:
    #     print(f'{repo.clone_url}, {repo.stargazers_count} stars')
 

def keyword_list(keywords=list()):
    keyword_splitter = lambda keyword:[keyword.strip() for keyword in keyword.split(',')]
    all_splitted_text = []
    if len(keywords)!=0:
        for word_list in keywords:
            all_splitted_text.append(keyword_splitter(word_list))
    return all_splitted_text

def write_to_csv(keywords):
    result = search_github(keywords)
    filename = "".join(keywords)+".txt"
    with open(filename,'w+') as f:
        for repo in result:
            if repo.stargazers_count>60:
                f.writelines(repo.clone_url+"\n")
                print("done")    

if __name__=="__main__":
    all_keywords = ["awesome,deep learning","awesome,machine learning","awesome,python","awesome,computer vision","awesome,nlp","awesome,supervised learning","awesome,RL",'awesome,Reinforcement learning']

    all_text = keyword_list(all_keywords)

    print(all_text)

    for i in all_text:
        write_to_csv(i)
        sleep(10)
