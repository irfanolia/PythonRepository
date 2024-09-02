def skill(skill_name):
    return f'{skill_name} is my favorite skill !'

def calculate_salary(base_salary, bonus_salary=0.1): # second argument is optional with default value of 0.1
    total_salary = base_salary + bonus_salary*base_salary
    return total_salary