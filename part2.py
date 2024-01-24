class Employee:
    def __init__(self, Emp_ID, Name, Age, Salary):
        self.Emp_ID = Emp_ID
        self.Name = Name 
        self.Age = Age 
        self.Salary = Salary 
    
emp1 = Employee('161E90', 'Ramu', 35, 59000)
emp2 = Employee('171E22', 'Tejas', 30, 82100)
emp3 = Employee('171G55', 'Abhi', 25, 100000)
emp4 = Employee('152K46', 'Jaya', 32, 85000)
employees = [emp1, emp2, emp3, emp4]

choice = int(input("Enter 0 to sort by age, 1 to sort by Name, 2 to sort by Salary"))
if choice == 0:
    employees.sort(key=lambda x: x.Age, reverse=True)
if choice == 1:
    employees.sort(key=lambda x: x.Name, reverse=True)
if choice == 2:
    employees.sort(key=lambda x: x.Salary, reverse=True)
for employee in employees:
    print(employee.Age, employee.Name, employee.Salary)





