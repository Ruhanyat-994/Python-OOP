'''A very basic sample class'''
class Employee : # it's a blue print
    name = "Ruhanayt"#it,s a class attribute
    marks = 34
    center = "Dhaka"

Employee.name = "RuhanyatNew"
ruhanyat = Employee() # A basic object
labib = Employee()
print(labib.name)

print(ruhanyat.name)

labib.name = "Labib"#setting a instance attribute to labib
print(labib.name)
print(ruhanyat.name)