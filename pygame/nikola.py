class Nikita:
    __slots__ = ['age','name']
    def __init__(self,name,age):
        self.age = 0
        self.name = "Никита"
    
        if name == "Никита" or name == "никита":
            print("меня зовут Никита")
        else:
            print("Меня зовут не " + name + " а Никита")
name = input("введите имя: ")
age = int(input("введите возраст: "))
nikita = Nikita(name,age)
try:
    nikita.surname = "Efimov"
except:
    print("так нельзя")