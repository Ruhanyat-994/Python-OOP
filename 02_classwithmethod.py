'''A very basic sample class'''
class Employee : # it's a blue print
    name = "Ruhanayt"
    marks = 34
    center = "Dhaka"

    def printObj(self):
        print(f"The name is {self.name}")

ruhanyat = Employee() # A basic object
print(ruhanyat.marks)
print(ruhanyat.center)
print(ruhanyat.name) 

ruhanyat.printObj()