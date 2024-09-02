class BaseSalary:
  def __init__(self, base_salary, bonus_rate=0.1, symbol="$"):
    self.base_salary = base_salary
    self.bonus_rate = bonus_rate
    self.symbol = symbol
    self.total_salary = base_salary * (1 + bonus_rate)
    self.bonus = self.total_salary - self.base_salary

  def __repr__(self):
    return f'Salary:{self.symbol}{self.base_salary:,.0f}'

  def show_salary(self):
    return f'Total Salary:{self.symbol}{self.total_salary:,.0f}'

  def show_bonus(self):
    return f'Bonus:{self.symbol}{self.bonus:,.0f}'

salary = BaseSalary(100000,0.2)

print(salary)
print(salary.show_salary())
print(salary.show_bonus())