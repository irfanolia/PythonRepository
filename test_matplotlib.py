import matplotlib.pyplot as plt
import numpy as np
from datasets import load_dataset
import pandas as pd

dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# data clean up
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)
date_counts = df.job_posted_date.value_counts()
date_counts = date_counts.sort_index()
df['job_posted_month'] = df['job_posted_date'].dt.month
monthly_counts = df.job_posted_month.value_counts()
monthly_counts = monthly_counts.sort_index()
#job_counts = df.job_title_short.value_counts().head(3)
job_counts = df.job_title_short.value_counts()
job_counts = job_counts.sort_values(ascending=True)
print(monthly_counts)
x = [1,2,3,4]
y = [1,2,3,4]

series = pd.Series([10,20,30,40,50], index=['a','b','c','d','e'])
print(series)

#x = np.arange(0,5,.1)
#y = np.sin(x)
#plt.plot(x,y)
#plt.plot(df.job_posted_date,df.job_posted_date)
#plt.plot(date_counts.index, date_counts)
#plt.plot(monthly_counts.index, monthly_counts.values)
#plt.bar(job_counts.index, job_counts)

plt.bar(job_counts.index, job_counts)
#plt.barh(job_counts, job_counts.index)
plt.title('Posting by Job Title')
plt.ylabel('Job Counts')
plt.xlabel('Job Titles')
plt.xticks(rotation=45, ha='right')
plt.show()