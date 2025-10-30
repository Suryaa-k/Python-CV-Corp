#Create a class Employee with:
#instance attributes: name, base_salary
#class variable: bonus_rate = 0.1
#instance method: final_salary() → base_salary + (base_salary × bonus_rate)
#class method: update_bonus(cls, new_rate) → updates bonus for all employees
#static method: is_valid_salary(sal) → checks if salary > 0
#Create two employees, show final salaries, update bonus rate, and show again.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

