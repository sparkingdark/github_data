from github import Github
 
ACCESS_TOKEN = '6e9d18c39a5574590a7b1ec6b780ac3167f835fc'
 
g = Github(ACCESS_TOKEN)
 
 
def search_github(keywords):
    query = '+'.join(keywords) + '+in:readme+in:description'
    result = list(g.search_repositories(query, 'stars', 'desc'))
 
    #print('Found {}repo(s)'.format(result.totalCount))

    return result
 
    # for repo in result:
    #     print(f'{repo.clone_url}, {repo.stargazers_count} stars')
 
 
if __name__ == '__main__':
    keywords = input('Enter keyword(s)[e.g python, flask, postgres]: ')
    keywords = [keyword.strip() for keyword in keywords.split(',')]
    result = search_github(keywords)
    with open('links.txt','a+') as f:
        for repo in result:
            if repo.stargazers_count>60:
                f.writelines(repo.clone_url+"\n")
                #print(f'{repo.clone_url}, {repo.stargazers_count} stars')