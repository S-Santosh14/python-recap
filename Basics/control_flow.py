# Simple if

age = 21
if age >= 18:
    print("Eligible to vote")

# if else

n = 7
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# if elif else

marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

# Nested if

username = "Santosh"
password = "1234"

if username == "Santosh":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid User")

# Ternary Operator

age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)

# Match Case

day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")