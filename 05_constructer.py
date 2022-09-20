'''A very basic sample class'''
class Employee : # it's a blue print
    def __init__(self,name,marks):

        self.name=name
        self.marks = marks
      

    def printObj(self):
        print(f"The name is {self.name}")
        print(f"The marks is {self.marks}")

    @staticmethod 
    def greet():
        print("Good day")

ruhanyat = Employee("Ruhanyat",34)
ruhanyat.printObj()