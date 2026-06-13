# For Loop

for i in range(1, 6):
    print(i)

# While Loop

i = 1
while i <= 5:
    print(i)
    i += 1

# Break

for i in range(1, 11):
    if i == 6:
        break
    print(i)

# Continue

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Pass

for i in range(3):
    pass

print("Pass executed")

# Enumerate

names = ["Santosh", "Rahul", "Kiran"]

for index, name in enumerate(names):
    print(index, name)

# Nested Loops

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# Pattern

for i in range(1, 6):
    print("*" * i)