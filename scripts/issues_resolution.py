import pandas as pd
# data=pd.read_csv(filepath)
# print(data.head())
open_issues=data['No_of_open_issues']
closed_issues=data['No_of_closed_issues']

data.drop('url',axis=1,inplace=True)
data.drop('topics',axis=1,inplace=True)
data.drop('user_name',axis=1,inplace=True)
total_issues=open_issues + closed_issues
data["total_issues"]=total_issues




data.drop(data.index[(data['total_issues']<100)],inplace=True)


data['issue_resolution_rate']=closed_issues/total_issues
data.sort_values(by=['issue_resolution_rate'],ascending=False,inplace=True)
# data.to_csv('{destination file path}',index=False)
print(data.head(5))


# print(issue_resolution_rate.head())