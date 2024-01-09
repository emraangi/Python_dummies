# Using a basic list comprehension
squares = [x**2 for x in range(5)]
print("Basic List Comprehension:", squares)

# List comprehension with a condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("List Comprehension with Condition:", even_squares)

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [num for row in matrix for num in row]
print("Nested List Comprehension:", flattened_matrix)

# List comprehension with a function
words = ["hello", "world", "python"]
word_lengths = [len(word) for word in words]
print("List Comprehension with Function:", word_lengths)

# List comprehension with if-else
even_odd_labels = ["Even" if num % 2 == 0 else "Odd" for num in range(10)]
print("List Comprehension with If-Else:", even_odd_labels)

# Set comprehension
unique_squares = {x**2 for x in range(5)}
print("Set Comprehension:", unique_squares)

# Dictionary comprehension
word_lengths_dict = {word: len(word) for word in words}
print("Dictionary Comprehension:", word_lengths_dict)

# List comprehension with zip
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined_list = [(num, char) for num, char in zip(list1, list2)]
print("List Comprehension with Zip:", combined_list)


