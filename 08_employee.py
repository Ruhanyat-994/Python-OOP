
class Employee:
    company = "Google"
    salary=100
     
ruhanyat = Employee()
labib = Employee()
ruhanyat.salary = 300
labib.salary= 400
print(ruhanyat.salary)
print(labib.salary)
print(labib.company)
print(ruhanyat.company)
Employee.company = "Youtube"
print(labib.company)
print(ruhanyat.company)