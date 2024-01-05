# 1. Function definition
def greet_person(name):
    """
    This function takes a person's name as a parameter and prints a greeting.

    Parameters:
    - name (str): The name of the person.
    """
    greeting = "Hello, " + name + "!"
    print(greeting)

# Calling the function
greet_person("Ram")
greet_person("Shaam")
greet_person("Charlie")

# 2. Function with Parameters:
#  A function that takes one or more parameters.
def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is: {result}")

# Call the function with arguments
add_numbers(3, 5)

# 3. Function with Default Parameters:
# A function with default parameter values.

def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

# Call the function without providing an argument
greet_with_default()


# 4. Function with Variable Number of Arguments (*args):
# A function that accepts a variable number of arguments.

def print_arguments(*args):
    for arg in args:
        print(arg)

# Call the function with multiple arguments
print_arguments("apple", "banana", "cherry")

# 5. Function with Return Value:
# A function that returns a value.
def square(number):
    return number ** 2

# Call the function and use the returned value
result = square(4)
print(f"The square of 4 is: {result}")

# 6. Function with Multiple Return Values:  A function that returns multiple values as a tuple.
def rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Call the function and unpack the returned values
area, perimeter = rectangle_properties(5, 3)
print(f"Area: {area}, Perimeter: {perimeter}")


# 7. Lambda Function: A small, anonymous function defined using the lambda keyword.
multiply = lambda x, y: x * y

# Call the lambda function
result = multiply(2, 3)
print(f"The product of 2 and 3 is: {result}")



