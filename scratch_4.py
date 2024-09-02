import job_analyzer
from job_analyzer import calculate_salary
from statistics import mean, median, mode
from datetime import datetime
import ast
import pandas as pd
import pyjokes

#from math import *


#print(my_module.skill_list)

#print(my_module.skill('Python'))
print(job_analyzer.skill('Python'))

print(calculate_salary(100000))

salary_list = [100000,50000,20000,150000,90000]
print('Salary mean =' , mean(salary_list))
print('Salary mode=' , mode(salary_list))
print('Salary median=' , median(salary_list))

data_science_jobs = [
    {'job_title': 'Data Scientist', 'job_skills': "['Python', 'SQL', 'Machine Learning']", 'job_date': '2023-05-12'},
    {'job_title': 'Machine Learning Engineer', 'job_skills': "['Python', 'TensorFlow', 'Deep Learning']", 'job_date': '2023-05-15'},
    {'job_title': 'Data Analyst', 'job_skills': "['SQL', 'R', 'Tableau']", 'job_date': '2023-05-10'},
    {'job_title': 'Business Intelligence Developer', 'job_skills': "['SQL', 'PowerBI', 'Data Warehousing']", 'job_date': '2023-05-08'},
    {'job_title': 'Data Engineer', 'job_skills': "['Python', 'Spark', 'Hadoop']", 'job_date': '2023-05-18'},
    {'job_title': 'AI Specialist', 'job_skills': "['Python', 'PyTorch', 'AI Ethics']", 'job_date': '2023-05-20'}
]

print('Date time Now is', datetime.now())

test_date = data_science_jobs[0]['job_date']
print(datetime.strptime(test_date,'%Y-%m-%d'))

for job in data_science_jobs:
    job['job_date'] = datetime.strptime(job['job_date'],'%Y-%m-%d')
    job['job_skills'] = ast.literal_eval(job['job_skills'])
    print(job['job_date'])
    print(job['job_skills'])

#print(data_science_jobs)

#file = open('housing.csv')
#content = file.read()
content = pd.read_csv('housing.csv')
print(content)
print(content['total_bedrooms'].sum())
print(pyjokes.get_joke())
#file.close()
