from sqlite3 import ProgrammingError


class Programmer:
    def __init__(self,name,language,):
        self.name = name 
        self.language = language

Ruhanyat=Programmer("Ruhanyat","Python")
Piash = Programmer("Piash","Java")

print(Ruhanyat.name)
print(Piash.name)
print(Ruhanyat.language)
print(Piash.language)