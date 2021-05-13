from pydriller import RepositoryMining as RM
import pandas as pd
import os
import datetime
dates=[]
# data=pd.read_csv({filepath},index_col=None)
repo_url=data['url']
df_commits=pd.DataFrame()
for repo in repo_url:
    for commit in RM(repo).traverse_commits():
        dates.append(commit.author_date)
#     # print('Hash {}, author {} , date{} '.format(commit.hash, commit.author.name , commit.author_date))
# print(dates[1].split(' '))
    with open('demo.txt', 'w') as f:
      for item in dates:
        f.write("%s\n" % item)
    f.close()

# today = datetime.date.today()
# # someday = datetime.date(2020, 12, 25)
    years=[]
    months=[]
    days=[]
# # print(diff.days)
    with open('demo.txt','r') as f:
        content=f.readlines()
        f.close()
    for line in content:
        split1=line.split("-")
        year=split1[0]
        years.append(int(year))
        month=split1[1]
        months.append(int(month))
        temp=split1[2].split(" ")
        day=temp[0]  
        days.append(int(day))
    x=datetime.date(years[0],months[0],days[0])
    y=datetime.date(years[-1],months[-1],days[-1])
    diff=(y-x).days
    n=len(years)
    freq=(n/diff)*30 #monthly frequency
    df_commits=df_commits.append({
        'repo_url':repo,
        'number_of_commits':n,
        'monthly_update_freq':freq,

    },ignore_index=True)
    os.remove('demo.txt')

# df_commits.to_csv({destination-folder-path},index=False)



#     # temp2=f.readline(1).split("-")
#     # day1=datetime.date(int(temp1[0]),int(temp1[1]),int(temp1[2]))
#     # day2=datetime.date(int(temp2[0]),int(temp2[1]),int(temp2[2]))
# # diff = day2 - day1
# # print(diff)
# # print(temp1)
