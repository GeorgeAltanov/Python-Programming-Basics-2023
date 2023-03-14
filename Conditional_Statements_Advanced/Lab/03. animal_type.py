name_of_animal = input()

class_of_animal = None

if name_of_animal == "dog":
    class_of_animal = "mammal"
elif name_of_animal == "crocodile" or name_of_animal == "tortoise" or name_of_animal == "snake":
    class_of_animal = "reptile"

else:
    class_of_animal = "unknown"

print(class_of_animal)
