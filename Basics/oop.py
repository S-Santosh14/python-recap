# Class and Object

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Santosh", 21)
s1.display()


# Inheritance

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("I am", self.name)


class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def work(self):
        print(f"{self.name} works at {self.company}")


e1 = Employee("Santosh", "Google")
e1.introduce()
e1.work()


# Polymorphism

class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


for animal in [Dog(), Cat()]:
    animal.sound()


# Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(1000)
acc.deposit(500)
print("Balance:", acc.get_balance())


# Class Variable

class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand


c1 = Car("Toyota")
c2 = Car("Honda")

print("Wheels:", Car.wheels)


# Static Method

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b


print("Sum:", MathUtils.add(10, 20))


# Method Overriding

class Animal:
    def speak(self):
        print("Animal Sound")


class Lion(Animal):
    def speak(self):
        print("Roar")


lion = Lion()
lion.speak()