class DataScienceJobsList:

    def __init__(self, jobs):
        '''
                    Initializes the DataScienceJobsList object with a list of jobs.
        '''
        self.jobs = jobs

    def __str__(self):
        '''
        Returns a string representation of the data science jobs list.
        '''
        jobs_str = 'Data Science Jobs:\n'
        for job in self.jobs:
            # Assuming job_skills is initially a string; it will be split later
            jobs_str += f"- {job['job_title']}: {job['job_skills']}\n"
        return jobs_str

    def split_skills(self):
        for job in self.jobs:
            job['job_skills'] = job['job_skills'].split(', ')

    def display_jobs(self):
        for job in self.jobs:
                print(f"Job Title: {job['job_title']}")
                print("Required Skills:")
                for skill in job['job_skills']:
                    print(f"- {skill}")
                print()  # Adds an empty line for better readability

data_science_jobs = [
    {'job_title': 'Data Scientist', 'job_skills': "Python, SQL, Machine Learning"},
    {'job_title': 'Data Analyst', 'job_skills': "SQL, Excel, Python"},
    {'job_title': 'Machine Learning Engineer', 'job_skills': "Python, TensorFlow, Keras"}
]


#jobs_list = DataScienceJobsList(data_science_jobs)
#print(jobs_list)
#jobs_list.split_skills()
#print(jobs_list)
#jobs_list.display_jobs()

jobs_list = DataScienceJobsList(data_science_jobs)
jobs_list.display_jobs()
jobs_list.split_skills()
jobs_list.display_jobs()
