# Basic Function

def hello():
    print("Hello, Santosh!")

hello()

# Function with Parameters

def sum(a, b):
    return a + b

print("Sum:", sum(10, 20))

# Default Arguments

def greet_user(name="Guest"):
    print("Welcome", name)

greet_user()
greet_user("Santosh")

# Keyword Arguments

def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=21, name="Santosh")

# Variable Length Arguments (*args)

def find_sum(*args):
    return sum(args)

print(find_sum(1, 2, 3))
print(find_sum(1, 2, 3, 4, 5))

# Keyword Variable Arguments (**kwargs)

def display(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display(name="Santosh", age=21, city="Hyderabad")

# Lambda Functions

square = lambda x: x * x

print("Square:", square(5))

# Map

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("Squares:", squares)


# Filter

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)


# Recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))

# Function Returning Multiple Values

def get_min_max(nums):
    return min(nums), max(nums)

minimum, maximum = get_min_max([10, 20, 30, 40])

print("Min:", minimum)
print("Max:", maximum)