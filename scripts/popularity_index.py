import requests
from github import Github
import pprint
import pandas as pd
token='{your github token}'
git=Github(token)
result = git.search_repositories('topic:machine-learning','stars','desc')
print(f'Found {result.totalCount} repo(s)')
repo_list=[]
 
for repo in result[0:100]:
    repo_list.append(repo.full_name)

def extract_project_info():
    df_project=pd.DataFrame()
    for i in repo_list:
        repo=git.get_repo(i)
        PRs=repo.get_pulls(state='all')
        # content=repo.get_forks
       
        
        
        
        df_project=df_project.append({
            'Name':repo.name,
            'user_name':repo.owner.login,
            'url':repo.clone_url,
            'stars':repo.stargazers_count,
            'viewers':repo.watchers_count,
            'forks':repo.get_forks().totalCount,
            'Populaity_index':0.4*repo.stargazers_count + 0.3*repo.watchers_count + 0.3*repo.get_forks().totalCount,



            
            
        },ignore_index=True)

    return df_project


df_project=extract_project_info()
print(df_project.head(20))
print(len(df_project))

df_project.to_csv('{destination file path}',sep=',',encoding='utf-8',index=False)
