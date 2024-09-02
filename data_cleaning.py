import matplotlib.pyplot as plt
import numpy as np
from datasets import load_dataset
import pandas as pd

dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# data clean up
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)

job_salary = df.groupby('job_title_short')['salary_year_avg'].median().sort_values()
job_salary.plot(kind='barh')
plt.title('Median Salary by Job Title')
plt.ylabel('Job Title')
plt.xlabel('Median Salary Average')
plt.show()