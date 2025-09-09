#tuples in python
#tuples are similar to lists but they are immutable
#you cannot change, add, or remove elements from a tuple once it is created
#when to use tuples:
#1. when you want to ensure that the data cannot be modified
#2. when you want to use the tuple as a key in a dictionary (lists cannot be used as keys)
#3. when you want to return multiple values from a function

my_tuple = (1, 2, 3,"green", 5.345, True)

print("Original tuple:", my_tuple, type(my_tuple))
#accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

#slicing a tuple
print("Sliced tuple (1 to 3):", my_tuple[1:4])
#tuples are immutable, so the following line would raise an error if uncommented
#my_tuple[2] = 10 #this will raise an error
#print("Modified tuple:", my_tuple)
#you can create a new tuple instead
new_tuple = my_tuple[:2] + (10,) + my_tuple[3:]
print("New tuple:", new_tuple)
print("Length of tuple:", len(my_tuple))
#tuple methods
print("Count of 2 in tuple:", my_tuple.count(2))
print("Index of 'green' in tuple:", my_tuple.index("green"))
#iterating through a tuple
for item in my_tuple:
    print("Tuple item:", item)
#checking membership
print("Is 5.345 in the tuple?", 5.345 in my_tuple)
print("Is 'blue' in the tuple?", "blue" in my_tuple)
#packing and unpacking tuples
a, b, c, d, e, f = my_tuple
print("Unpacked values:", a, b, c, d, e, f)
#nested tuples
nested_tuple = (1, 2, (3, 4), (5,
    6))
print("Nested tuple:", nested_tuple)
print("Accessing nested element:", nested_tuple[2][1])
#tuples can be used as keys in dictionaries
my_dict = {("a", 1): "value1", ("b", 2): "value2"}
print("Dictionary with tuple keys:", my_dict)
print("Value for key ('a', 1):", my_dict[("a", 1)])
#tuples are generally more memory efficient than lists  
import sys
list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)
print("Memory size of list:", sys.getsizeof(list_example))
print("Memory size of tuple:", sys.getsizeof(tuple_example))
#tuples are faster than lists for certain operations due to their immutability
import timeit

list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000) 
print("Time taken to create a list:", list_time)
print("Time taken to create a tuple:", tuple_time)
#Note: While tuples are immutable, if they contain mutable elements (like lists), those elements can be modified.
#However, the structure of the tuple itself cannot be changed.
mutable_in_tuple = (1, 2, [3, 4])
print("Original tuple with mutable element:", mutable_in_tuple)
mutable_in_tuple[2].append(5)
print("Modified tuple with mutable element:", mutable_in_tuple)    
#This shows that while the tuple structure is immutable, the mutable element inside it can be changed.
#Tuples are a fundamental data structure in Python and are widely used in various applications, including
#function returns, data integrity, and as keys in dictionaries.
#They provide a way to group related data together in a way that ensures the data cannot be altered.
#Understanding tuples is essential for effective Python programming and data manipulation.
#Tuples can also be used in conjunction with other data structures and functions to create more complex data models.
#Tuples can be nested within other tuples, lists, or dictionaries to create multi-dimensional data
#structures, making them versatile for various programming needs.
#Tuples can also be used in functions to return multiple values, making it easy to handle related data.
def min_max(numbers):
    return (min(numbers), max(numbers)) 
result = min_max([1, 2, 3, 4, 5])
print("Min and Max values:", result)
min_value, max_value = result
print("Unpacked Min value:", min_value)
print("Unpacked Max value:", max_value)
#This demonstrates how tuples can be used to return and unpack multiple values from a function.

