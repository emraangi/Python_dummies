# Variant 1: Simple if statement
age = 25

if age >= 18:
    print("You are an adult.")

# Variant 2: if-else statement
num = 10

if num % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")

# Variant 3: if-elif-else statement
score = 85

if score >= 90:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
else:
    print("Grade: C")

# Variant 4: Nested if statements
num = 15

if num > 0:
    print("Number is positive.")
    if num % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
else:
    print("Number is non-positive.")

# Variant 5: Multiple conditions with logical operators
temperature = 28

if temperature > 30 and temperature <= 40:
    print("It's a warm day.")
elif temperature > 40:
    print("It's a hot day.")
else:
    print("It's a cool day.")

# Variant 6: Ternary operator for concise if-else
is_adult = True
message = "You are an adult." if is_adult else "You are a minor."
print(message)

# Variant 7: Checking for membership with 'in'
fruits = ['apple', 'banana', 'cherry']

if 'banana' in fruits:
    print("Banana is in the list.")

