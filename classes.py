from argparse import Namespace

# Example of independent class (base class)
class Person:
    def __init__(self, first_name, last_name, age, likes_pizza):
        # Member declaration and initialization
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.likes_pizza = likes_pizza
       
    # Methods
    def walk(self):
        print("Walking...")
        
    def run(self):
        print("Running...")
        
# Example of class inheritance
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
        
    def speak(self):
        print("I don't know what I say")
        
class Cat(Pet):
    def __init__(self, name, age, color = "brown"):
        super().__init__(name, age)
        self.color = color
        
    def speak(self):
        print("Meow")
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
        
class Dog(Pet):
    def speak(self):
        print("Bark")
        
