class Employee:
    company="Google"
    def getSalary(self ):
        print("Salary is 100k")

ruhanyat=Employee()
ruhanyat.getSalary()
Employee.getSalary(ruhanyat)