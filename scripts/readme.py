import requests
from github import Github
import pprint
import pandas as pd
token='{your github token}'
git=Github(token)
result = git.search_repositories('topic:machine-learning','stars','desc')
print(f'Found {result.totalCount} repo(s)')
repo_list=[]
 
for repo in result[0:50]:
    repo_list.append(repo.full_name)

def extract_project_info():
    df_project=pd.DataFrame()
    for i in repo_list:
        repo=git.get_repo(i)
        commits = list(repo.get_commits("master"))[0:10]
       
        
        
        
        df_project=df_project.append({
            'Name':repo.name,
            'url':repo.clone_url,
            # 'readme':git.get_repo(str(i).strip()).get_readme().decoded_content
            'commit':commits

            
            
        },ignore_index=True)

    return df_project


df_project=extract_project_info()
print(df_project)

# df_project.to_csv({destination file path}',sep=',',encoding='utf-8',index=False)
