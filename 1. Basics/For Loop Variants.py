# Variants of For Loop in Python

# Variant 1: Iterating over a sequence (e.g., list)
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

# Variant 2: Using the range() function
for i in range(5):  # Iterates from 0 to 4
    print(i)

# Variant 3: Iterating over a string
word = "Python"

for char in word:
    print(char)

# Variant 4: Iterating over a dictionary
person = {'name': 'John', 'age': 30, 'city': 'New York'}

for key, value in person.items():
    print(f"{key}: {value}")

# Variant 5: Enumerating elements using enumerate()
colors = ['red', 'green', 'blue']

for index, color in enumerate(colors):
    print(f"Color {index + 1}: {color}")

# Variant 6: Looping with zip() to iterate over multiple iterables
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# Variant 7: Looping in reverse using reversed()
numbers = [1, 2, 3, 4, 5]

for num in reversed(numbers):
    print(num)

# Variant 8: Using break and continue
for i in range(10):
    if i == 3:
        print("Skipping 3.")
        continue
    elif i == 7:
        print("Breaking at 7.")
        break
    print(i)
