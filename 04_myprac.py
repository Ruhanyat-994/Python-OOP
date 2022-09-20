class Student:
    Topper="Ruhanyat"
    Captain = "Labib"
    Teacher = "Luthfor"

Student.Captain= "Munem" # setting a class attribute
#class attribute is a personal property of class
District= Student()
Favorite_Place= Student()
Favorite_Dish= Student()

print(District.Captain)
print(Favorite_Dish.Teacher)
Favorite_Place.Topper="TarikJamil" # i'm setting an instance attribute
#Instance attribute is a personal property of object
print(Favorite_Place.Topper)