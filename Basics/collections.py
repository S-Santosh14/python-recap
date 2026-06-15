# Lists

l = [1, 2, 3, 4]

l.append(5)
l.remove(2)
l.sort()

print("List:", l)
print("First Element:", l[0])
print("Length:", len(l))

# Tuples

t = (10, 20)

print("\nTuple:", t)
print("First Element:", t[0])
print("Length:", len(t))

# Sets

s = {1, 2, 3, 2, 1}

s.add(4)

print("\nSet:", s)

# Dictionaries

student = {
    "name": "Santosh",
    "age": 21,
    "cgpa": 9.5
}

print("\nDictionary:", student)
print("Name:", student["name"])

student["city"] = "Hyderabad"

print("Keys:", student.keys())
print("Values:", student.values())

# List Comprehension

squares = [x * x for x in range(1, 6)]

print("\nList Comprehension:", squares)

# Dictionary Comprehension

mapping = {x: x * x for x in range(1, 6)}

print("\nDictionary Comprehension:", mapping)

# Set Comprehension

even_set = {x for x in range(10) if x % 2 == 0}

print("\nSet Comprehension:", even_set)

# Set Operations

a = {1, 2, 3}
b = {3, 4, 5}

print("\nUnion:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

# Useful Dictionary Methods

print("\nItems:")
for key, value in student.items():
    print(key, ":", value)

# Membership Operators

print("\nMembership:")
print(3 in l)
print("name" in student)

# Nested Collection

students = [
    {"name": "Santosh", "cgpa": 9.5},
    {"name": "Rahul", "cgpa": 8.8}
]

print("\nNested Collection:")
for s in students:
    print(s["name"], "-", s["cgpa"])