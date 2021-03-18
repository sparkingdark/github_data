
import re
import sys
import json
import threading
from requests import get
from requests.auth import HTTPBasicAuth

breach = None
uname = ''
jsonOutput = dict()

def findContributorsFromRepo(username, repo):
	response = get('https://api.github.com/repos/%s/%s/contributors?per_page=100' % (username, repo), auth=HTTPBasicAuth(uname, '')).text
	contributors = re.findall(r'https://github\.com/(.*?)"', response)
	return contributors

def findReposFromUsername(username):
	response = get('https://api.github.com/users/%s/repos?per_page=100&sort=pushed' % username, auth=HTTPBasicAuth(uname, '')).text
	repos = re.findall(r'"full_name":"%s/(.*?)",.*?"fork":(.*?),' % username, response)
	nonForkedRepos = []
	for repo in repos:
		if repo[1] == 'false':
			nonForkedRepos.append(repo[0])
	return nonForkedRepos

def findEmailFromContributor(username, repo, contributor):
	response = get('https://github.com/%s/%s/commits?author=%s' % (username, repo, contributor), auth=HTTPBasicAuth(uname, '')).text
	latestCommit = re.search(r'href="/%s/%s/commit/(.*?)"' % (username, repo), response)
	if latestCommit:
		latestCommit = latestCommit.group(1)
	else:
		latestCommit = 'dummy'
	commitDetails = get('https://github.com/%s/%s/commit/%s.patch' % (username, repo, latestCommit), auth=HTTPBasicAuth(uname, '')).text
	email = re.search(r'<(.*)>', commitDetails)
	if email:
		email = email.group(1)
		if breach:
			jsonOutput[contributor] = {}
			jsonOutput[contributor]['email'] = email
			if get('https://haveibeenpwned.com/api/v2/breachedaccount/' + email).status_code == 200:
				email = email + start + 'pwned' + stop
				jsonOutput[contributor]['pwned'] = True
			else:
				jsonOutput[contributor]['pwned'] = False
		else:
			jsonOutput[contributor] = email
	return email

def findEmailFromUsername(username):
    repos = findReposFromUsername(username)
    import time 
    time.sleep(1)
    for repo in repos:
        email = findEmailFromContributor(username, repo, username)
        if email:
            print (username + ' : ' + email)
            return email
            break

    #return "not found"    
    

def findEmailsFromRepo(username, repo):
	contributors = findContributorsFromRepo(username, repo)
	print ('%s Total contributors: %s%i%s' % (info, green, len(contributors), end))
	for contributor in contributors:
		email = (findEmailFromContributor(username, repo, contributor))
		if email:
			print (contributor + ' : ' + email)

def findUsersFromOrganization(username):
	response = get('https://api.github.com/orgs/%s/members?per_page=100' % username, auth=HTTPBasicAuth(uname, '')).text
	members = re.findall(r'"login":"(.*?)"', response)
	return members



if __name__=="__main__":
    import pandas as pd 

    df = pd.read_csv("./data.csv")
    users = df.owner
    project = df.repo
    emails = []

    for i,j in zip(users,project):
        print(i,j)
        targetUser=True
        if targetUser:
            # findEmailFromUsername(i)
            emails.append(findEmailFromUsername(i))
            print(findEmailFromUsername(i))
    df.insert(4,"email",emails)                
