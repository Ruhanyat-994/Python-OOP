class Employee:
    company="Google"
    def getSalary(self ):
        print(f"Salary for the employee working in {self.company} is  {self.salary}")
        
ruhanyat=Employee()

ruhanyat.salary=100000
Employee.getSalary(ruhanyat)
ruhanyat.getSalary()