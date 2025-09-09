# Functions in Python
# A function is a block of code that only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Defining a function
def my_function():
    print("Hello from my function!")

# Calling a function
my_function()

# Function with parameters
def greet(name):
    print("Hello,", name)

greet("Alice")
greet("Bob")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print("The sum is:", result)

# Function with default parameter value
def greet_with_default(name="Guest"):
    print("Hello,", name)
greet_with_default()
greet_with_default("Charlie")

# Function with variable number of arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
print("Sum of all numbers:", sum_all(1, 2, 3, 4, 5))
print("Sum of some numbers:", sum_all(10, 20, 30))

# Lambda functions (anonymous functions)
square = lambda x: x * x
print("Square of 4 is:", square(4))
print("Square of 7 is:", square(7))
# You can use lambda functions wherever function objects are required.
# They are often used for short, throwaway functions.
# Example of using lambda with map function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared numbers:", squared_numbers)
# Example of using lambda with filter function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Example of using lambda with sorted function
points = [(1, 2), (3, 1), (5, 4), (2, 3)]
sorted_points = sorted(points, key=lambda point: point[1])
print("Sorted points:", sorted_points)

# You can also assign functions to variables and pass them as arguments to other functions
def apply_function(func, value):
    return func(value)
result = apply_function(lambda x: x * 2, 10)
print("Result of applying function:", result)
# Functions can also be nested inside other functions
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()
outer_function("Hello from the outer function!")

# Functions can also be recursive, meaning they can call themselves
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5 is:", factorial(5))
print("Factorial of 7 is:", factorial(7))

# Note: Always ensure that recursive functions have a base case to prevent infinite recursion.
# Functions are a fundamental building block in Python and are essential for writing clean, modular, and reusable code.
# They help in breaking down complex problems into smaller, manageable pieces.

#call by reference vs call by value
#In Python, all arguments are passed by reference. However, the behavior can sometimes resemble call by value for immutable types.
#Mutable types (like lists and dictionaries) can be modified in place, while immutable types (
#like integers, floats, and strings) cannot be changed in place.
def modify_list(lst):
    lst.append(4)
    print("Inside function (list):", lst)
my_list = [1, 2, 3]
modify_list(my_list)
print("Outside function (list):", my_list)
def modify_number(num):
    num += 10
    print("Inside function (number):", num)
my_number = 5
modify_number(my_number)
print("Outside function (number):", my_number)

# In the first example, the list is modified inside the function, and the change is reflected outside the function.
# In the second example, the integer is not modified outside the function because integers are immutable.
# This demonstrates the difference between mutable and immutable types in Python.
# Understanding this distinction is crucial for effective function design and avoiding unintended side effects in your code.
# You can also use the global keyword to modify a global variable inside a function
global_var = 10
def modify_global():
    global global_var
    global_var += 5
    print("Inside function (global variable):", global_var)
modify_global()
print("Outside function (global variable):", global_var)
# However, use global variables sparingly as they can make code harder to understand and maintain.
# It's generally better to pass variables as parameters and return values from functions.
# This concludes the overview of functions in Python.
# You can explore more advanced topics like decorators, generators, and higher-order functions as you become more comfortable with Python functions.
# Happy coding!


