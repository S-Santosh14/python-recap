# Variables in Python

name = "Santosh"
age = 21
cgpa = 9.5
is_single = True
print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Placed:", is_single)

# Common Data Types

n1 = 100
n2 = 99.99
language = "Python"
flag = True
print(type(n1))
print(type(n2))
print(type(language))
print(type(flag))

# Arithmetic Operators

a = 15
b = 4
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# Comparison Operators

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical Operators

print(True and False)
print(True or False)
print(not True)

# Assignment Operators

x = 10
x += 5
print(x)

# Membership Operators

language = "Python"
print("P" in language)
print("Java" not in language)

# Identity Operators

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print(list1 is list2)
print(list1 is list3)

# Type Casting

age = "21"
print(type(age))
age = int(age)
print(type(age))
height = 5.8
height = int(height)
print(height)

# Taking Input from User

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name)
print("Your age is", age)