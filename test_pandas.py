import pandas as pd
from datasets import load_dataset

df = pd.read_csv('housing.csv')
#print(df)
#print(df['total_bedrooms'])
#print(df.total_bedrooms[2999])

#load_dataset(data_files='data_jobs.csv')
#load_dataset(None,None,None,data_files='data_jobs.csv')
#load_dataset('/Users/irfanolia/PycharmProjects/pythonPpstgresql/data_jobs')
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()
print(df.info())
#print(df.head(10))
#print(df.tail(10))
#print(df[['job_title_short','job_location']].head(5))
#print(df.iloc[90:100,1:2])
#print(df.describe())
#print(df.job_title_short.unique())
print(df[(df.job_title_short == 'Data Analyst') & (df.salary_year_avg > 100000)])
print(df.job_posted_date[0])
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)
#df.info()
print(df.job_posted_date.dt.month)
df['job_posted_month'] = df.job_posted_date.dt.month
print(df.info())
df.sort_values('job_posted_date', inplace =True)
#df.drop(labels='salary_hour_avg', axis=1, inplace=True)
print('salary hour average is dropped')
print(df.info())
#df.dropna(subset=['salary_year_avg'],inplace=True)
print(df.info())
df.sort_values(by='job_posted_date', ascending=False, inplace=True)
print(df['salary_year_avg'].describe())
print(df.count())
print(df['salary_year_avg'].mode())
#Now we are going to get the index value of the max value of salary_year_avg.
print(df['salary_year_avg'].idxmax())

print(df.iloc[50])
print('minimum salary is : ', df['salary_year_avg'].min())
print('minimum salary index is :', df['salary_year_avg'].idxmin())
min_salary_index = df['salary_year_avg'].idxmin()
print(df.iloc[min_salary_index])
print(df.salary_year_avg[min_salary_index])
print(df.job_title_short.value_counts())
print(df.groupby('job_title_short')['salary_year_avg'].min())
print(df.groupby('job_title_short')['salary_year_avg'].median())
#print(df.groupby(['job_title_short','job_country'])['salary_year_avg'].median())
print(df.groupby('job_title_short')[['salary_year_avg','salary_hour_avg']].median())
print(df.groupby('job_title_short')[['salary_year_avg','salary_hour_avg']].agg(['min','max']))
print('Now check this')
filtered_data_jobs = df[df['job_title_short'].str.contains('Data',case=False)]
print(filtered_data_jobs.groupby('job_title_short')[['salary_year_avg','salary_hour_avg']].agg(['min','max']))
print(df['job_country'].value_counts().head(10))
print(df['job_country'].isin(['Brazil']).any())
filtered_us_jobs = df[df['job_country'] == 'United States']
filtered_us_jobs = filtered_us_jobs[filtered_us_jobs['salary_year_avg'].notna()]
print(filtered_us_jobs)
print(filtered_us_jobs.groupby('job_title_short')[['salary_year_avg']].agg(['min','max','median','count']))
print(filtered_us_jobs.groupby('job_title_short')['salary_year_avg'].agg(['min','max','median','count']).sort_values(by='median', ascending=False))
#print(filtered_us_jobs.groupby('job_title_short')[['salary_year_avg']].count())