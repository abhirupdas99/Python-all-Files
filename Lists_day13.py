# Lists in Python
# A list is a collection of items that can be of different types.
# Lists are ordered, mutable, and allow duplicate elements.

# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Accessing elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Modifying elements
my_list[2] = 10
print("Modified list:", my_list)

# Adding elements
my_list.append(6)
print("List after appending:", my_list)

# Removing elements
my_list.remove(4)
print("List after removing:", my_list)

# Slicing a list
print("Sliced list (1 to 3):", my_list[1:4])

# List comprehension
squared = [x * x for x in my_list]
print("Squared list:", squared)

# Nested lists
nested_list = [[1, 2, 3], [4, 5, 6]]
print("Nested list:", nested_list)
print("Accessing nested element:", nested_list[1][2])

# List methods
print("List length:", len(my_list))
print("Max element:", max(my_list))
print("Min element:", min(my_list))

# Iterating through a list
for item in my_list:
    print("List item:", item)
# Checking membership
print("Is 10 in the list?", 10 in my_list)
print("Is 4 in the list?", 4 in my_list)
# Clearing a list
my_list.clear()
print("Cleared list:", my_list)
# Copying a list
copied_list = squared.copy()
print("Copied list:", copied_list)
# Extending a list
copied_list.extend([49, 64])
print("Extended list:", copied_list)
# Reversing a list
copied_list.reverse()
print("Reversed list:", copied_list)
# Sorting a list
copied_list.sort()
print("Sorted list:", copied_list)
# Finding the index of an element
index_of_25 = copied_list.index(25)
print("Index of 25 in the list:", index_of_25)
# Counting occurrences of an element
count_of_49 = copied_list.count(49)
print("Count of 49 in the list:", count_of_49)
# Nested list comprehension
flattened = [num for sublist in nested_list for num in sublist]
print("Flattened nested list:", flattened)
# Combining lists
combined_list = my_list + copied_list
print("Combined list:", combined_list)
# Replicating lists
replicated_list = [0] * 5
print("Replicated list:", replicated_list)
# List unpacking
a, b, c, d, e = copied_list[:5]
print("Unpacked values:", a, b, c, d, e)
# Lists can also be used with functions and methods
def sum_of_list(lst):
    return sum(lst)

print("Sum of copied list:", sum_of_list(copied_list))
# Lists are versatile and widely used in Python programming for various applications.
# They provide a way to store and manipulate collections of data efficiently.
# You can perform various operations on lists to suit your programming needs.
# Lists can also be nested, allowing for the creation of multi-dimensional arrays or matrices.
# Lists can be combined with other data structures like dictionaries and sets for more complex data handling.
# Lists can be used in conjunction with loops and conditional statements to perform iterative operations and filtering.
# Lists can be converted to other data types like tuples or sets when needed.
# Lists can also be used with built-in functions like map, filter, and reduce for functional programming.
# Lists can be serialized and deserialized using libraries like JSON for data storage and transmission.
# Lists can be used in various algorithms and data processing tasks, making them a fundamental part of Python programming.
# Lists can also be used in data analysis and scientific computing with libraries like NumPy and Pand
#as, which provide additional functionality for handling large datasets and performing complex operations.
# Lists can be nested to create multi-dimensional structures, which are useful in various applications like matrices and grids.
# Lists can be used to implement stacks, queues, and other data structures.
# Lists can be used in conjunction with other data structures like dictionaries and sets for more complex data handling.
# Lists can be used with list comprehensions to create new lists based on existing ones, allowing for concise and readable code.
# Lists can be used with slicing to extract specific portions of the list or to create sublists.
# Lists can be used with the zip function to combine multiple lists into a single list of tuples