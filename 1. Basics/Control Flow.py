# Control Flow in Python

# 1. Conditional Statements

# Example 1: if-else statement
num = 10

if num > 0:
    print("Number is positive.")
else:
    print("Number is non-positive.")

# Example 2: if-elif-else statement
grade = 75

if grade >= 90:
    print("Grade: A")
elif 80 <= grade < 90:
    print("Grade: B")
elif 70 <= grade < 80:
    print("Grade: C")
else:
    print("Grade: F")

# 2. Looping Constructs

# Example 1: for loop
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Example 2: while loop
print("\nCounting down from 5 to 1:")
count = 5
while count > 0:
    print(count)
    count -= 1

# Example 3: break and continue statements in a loop
print("\nLoop with break and continue:")
for i in range(1, 11):
    if i == 5:
        print("Breaking the loop at 5.")
        break
    elif i % 2 == 0:
        print(f"Skipping even number: {i}")
        continue
    print(f"Processing: {i}")

# Example 4: Nested loop
print("\nNested Loop:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()


