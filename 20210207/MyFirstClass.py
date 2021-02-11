class Animal:

    animalName = ""
    animalAge = 0

    #this is animal constructor
    # def __init__(self):
    #     print("Hi. this is Animal Constructor")

    #Overloaded constructors
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("Animal is eating....")
        print("Animal Name: " + self.name)
        print("Animal Age: " + self.age)
    
    def sleep(self):
        print("Animal is sleeping....")

    def run(self):
        print("Animal is running")

# human = Animal()
# human.eat()

# Animal dog = new Animal() 
cat = Animal("Kitty", "3")
cat.eat()