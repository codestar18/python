class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hii, I'm  {self.name}")


person1 = Person("Jayasree")
print(person1.name)
person1.talk()