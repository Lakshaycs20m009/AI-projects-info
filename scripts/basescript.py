import requests
from github import Github
import pprint
import pandas as pd
token=f'{Your-Github-token}'
git=Github(token)
result = git.search_repositories('topic:machine-learning','stars','desc') ##search keywords
print(f'Found {result.totalCount} repo(s)')
repo_list=[]
 
for repo in result[750:]:
    repo_list.append(repo.full_name)

def extract_project_info():
    df_project=pd.DataFrame()
    for i in repo_list:
        repo=git.get_repo(i)
        PRs=repo.get_pulls(state='all')
       
        
        
        
        df_project=df_project.append({
            'Name':repo.name,
            'user_name':repo.owner.login,
            'url':repo.clone_url,
            'No_of_open_issues':repo.get_issues(state='open').totalCount,
            'No_of_closed_issues':repo.get_issues(state='closed').totalCount,
            'topics':repo.get_topics()

            
            
        },ignore_index=True)

    return df_project


df_project=extract_project_info()
print(len(df_project))

# df_project.to_csv('{destination file path}',sep=',',encoding='utf-8',index=False)
