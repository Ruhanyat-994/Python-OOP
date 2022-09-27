class Employee:
    company="Google"
    def getSalary(self ):
        print(f"Salary is {self.salary}")
        
ruhanyat=Employee()

ruhanyat.salary=100000
Employee.getSalary(ruhanyat)