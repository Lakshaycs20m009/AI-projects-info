import pandas as pd
data=pd.read_csv('filepath')
# print(data.head())

data.drop('No_of_open_issues',axis=1,inplace=True)
data.drop('No_of_closed_issues',axis=1,inplace=True)
data.drop('total_issues',axis=1,inplace=True)
data.drop('user_name',axis=1,inplace=True)
data.drop('url',axis=1,inplace=True)
data.to_csv('/Users/lakshaykalra/Desktop/topics.csv',index=False)


# print(issue_resolution_rate.head())