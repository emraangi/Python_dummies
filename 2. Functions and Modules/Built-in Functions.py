# 1. len() - Returns the length of an object (number of items in an iterable).
example_list = [1, 2, 3, 4, 5]
length_of_list = len(example_list)
print("Length of list:", length_of_list)

# 2. type() - Returns the type of an object.
example_variable = 42
variable_type = type(example_variable)
print("Type of variable:", variable_type)

# 3. max() - Returns the largest item in an iterable or the largest of two or more arguments.
max_value = max(5, 8, 2, 11)
print("Maximum value:", max_value)

# 4. min() - Returns the smallest item in an iterable or the smallest of two or more arguments.
min_value = min(5, 8, 2, 11)
print("Minimum value:", min_value)

# 5. sum() - Returns the sum of all items in an iterable.
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = sum(numbers)
print("Sum of numbers:", sum_of_numbers)

# 6. sorted() - Returns a sorted list from the specified iterable.
unsorted_list = [3, 1, 4, 1, 5, 9, 2]
sorted_list = sorted(unsorted_list)
print("Sorted list:", sorted_list)

# 7. range() - Generates a sequence of numbers within a specified range.
sequence_of_numbers = list(range(1, 6))
print("Sequence of numbers:", sequence_of_numbers)

# 8. abs() - Returns the absolute value of a number.
negative_number = -10
absolute_value = abs(negative_number)
print("Absolute value:", absolute_value)

# 9. round() - Rounds a number to the nearest integer or to the specified number of decimals.
pi_approximation = 3.14159
rounded_pi = round(pi_approximation, 2)
print("Rounded pi:", rounded_pi)

# 10. input() - Reads a line from the console and returns it as a string.
user_input = input("Enter your name: ")
print("Hello, " + user_input + "!")
