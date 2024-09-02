# Import Package
import numpy as np
import random

# Example: An array representing the number of years of experience required for three different data science job listings.
years_of_experience = np.array([1, 2, 3, 4, 5])

print(years_of_experience)
years_of_experience_plus_one = years_of_experience + 1
print(years_of_experience_plus_one)
years_of_experience_minus_one = years_of_experience - 1
print(years_of_experience_minus_one)
years_of_experience_half = years_of_experience / 2
print(years_of_experience_half)
years_of_experience_double = years_of_experience * 2
print(years_of_experience_double)
# Example: Selecting the experience requirement for the second and third job listings.
second_and_third_jobs_experience = years_of_experience[1:3]
print(second_and_third_jobs_experience)
# Example: Selecting only those job listings that require more than 1 year of experience.
jobs_with_more_than_one_year_exp = years_of_experience[years_of_experience > 2]
print(jobs_with_more_than_one_year_exp)

#First lets create a list with 10 yearly salaries for a Senior Data Analyst job.
# We're just using a combination of the random library to get random integers between 100000 and 150000.
# Then using a for loop to get 10 (random) values.
salary = [random.randint(100000, 150000) for num in range(10)]
print(salary)
#Now we'll convert this list into a NumPy array.
salary_array = np.array(salary)
print(salary_array)

#Calculate the total sum of the elements in the salary_array.
total_sum_salaries = np.sum(salary_array)
print(total_sum_salaries)

# This is a conceptual example since taking the product of a boolean series isn't common
product_salaries = np.prod(salary_array)
print(product_salaries)

#Calculates the cumulative sum of elements of the salary_array.
# It calculates the cumulative sum at each index,
# meaning each element in the output array is the sum of all preceding elements including the current one from the original array.
cumulative_sum_salaries = np.cumsum(salary_array)
print(cumulative_sum_salaries)

# Cumulative product of 'job_no_degree_mention' column (conceptual example)
cumulative_prod_salaries = np.cumprod(salary_array)
print(cumulative_prod_salaries)

#Calculate the average salary in the salary_array.
average_salary = np.mean(salary_array)
print(average_salary)

#job titles
jobs_tiles = np.array(['Data Scientist','Data Analyst', 'Data Engineer', 'Machine Learning Engineer', 'AI Engineer'])

#Base Salaries
base_salaries = np.array([100000, 105000, 110000, 150000, np.nan])

#bonus rates
bonus_rates = np.array([.1,.2,.3,.15, np.nan])

total_salary = base_salaries * (1+ bonus_rates)

print(total_salary)
print(np.nanmean(total_salary))


