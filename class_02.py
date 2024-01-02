# 클래스 상속

class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("move")
    def speak(self):
        pass

class Dog (Animal):
    def speak(self):
        print("bark")

class Duck (Animal):
    def speak(self):
        print("quack")
    
dog = Dog("doggy")
n = dog.name
dog.move()
dog.speak()

#클래스 다형성
animals = [Dog('sky'), Duck('duck')]

for a in animals:
    a.speak()

