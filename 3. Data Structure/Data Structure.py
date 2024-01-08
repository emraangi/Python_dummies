# List Example
my_list = [1, 2, 3, 'hello', 5.5]
print("List:", my_list)

# Tuple Example
my_tuple = (1, 2, 'world', 3.14)
print("Tuple:", my_tuple)

# Set Example
my_set = {1, 2, 3, 4, 4, 5}
print("Set:", my_set)

# Dictionary Example
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print("Dictionary:", my_dict)

# String Example
my_string = 'Hello, World!'
print("String:", my_string)

# Array Example
from array import array
my_array = array('i', [1, 2, 3, 4, 5])
print("Array:", my_array)

# Deque Example
from collections import deque
my_deque = deque([1, 2, 3])
my_deque.append(4)
my_deque.appendleft(0)
print("Deque:", my_deque)

# Stack Example
stack = []
stack.append(1)
stack.append(2)
stack.pop()
print("Stack:", stack)

# Queue Example
from queue import Queue
my_queue = Queue()
my_queue.put(1)
my_queue.put(2)
my_queue.get()
print("Queue:", list(my_queue.queue))
