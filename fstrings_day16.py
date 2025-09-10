# f-strings are intoduced in Python 3.6 and later versions
# they provide a way to embed expressions inside string literals, using curly braces {}

#example 1: basic usage
name = "Alice"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")

#example 2: expressions inside f-strings
width = 5
height = 10
area = width * height
print(f"The area of a rectangle with width {width} and height {height} is {area}.")

#example 3: formatting numbers
pi = 3.141592653589793
print(f"The value of pi is approximately {pi:.2f}.")  # rounds to 2 decimal places
print(f"The value of pi in scientific notation is {pi:.3e}.")  # scientific notation
print(f"The value of pi with leading zeros is {pi:08.3f}.")  # total width 8, 3 decimal places, leading zeros
print(f"The value of pi as percentage is {pi:.2%}.")  # percentage format
print(f"The value of pi in hexadecimal is {pi:#x}.")  # hexadecimal format
print(f"The value of pi in binary is {int(pi):b}.")  # binary format
print(f"The value of pi in octal is {int(pi):o}.")  # octal format
print(f"The value of pi with comma as thousand separator is {1000000*pi:,.2f}.")  # comma as thousand separator



#example 4: using f-strings with dictionaries
person = {"name": "Bob", "age": 25}
print(f"{person['name']} is {person['age']} years old.")

#example 5: using f-strings with lists
fruits = ["apple", "banana", "cherry"]
print(f"My favorite fruits are: {', '.join(fruits)}.")
print(f"The first fruit is {fruits[0]} and the last fruit is {fruits[-1]}.")
#example 6: using f-strings with function calls
def greet(name):
    return f"Hello, {name}!"
print(f"{greet('Charlie')} Welcome to the f-string tutorial.")
#example 7: multi-line f-strings
multiline = f"""This is a multi-line f-string.
It can span multiple lines.
You can include variables like {name} and {age}."""
print(multiline)
#example 8: nested f-strings
nested = f"The area of a rectangle is {f'{width} * {height} = {width * height}'}."
print(nested)
#example 9: using f-strings with datetime
from datetime import datetime
now = datetime.now()
print(f"Current date and time: {now:%Y-%m-%d %H:%M:%S}")
#example 10: using f-strings with escape sequences
path = "C:\\Users\\Alice\\Documents"
print(f"The file path is: {path}")
quote = 'He said, "Hello!"'
print(f'She replied, "{quote}"')
#example 11: using f-strings with raw strings
raw_string = r"C:\Users\Alice\Documents"
print(f"The raw string is: {raw_string}")
#example 12: using f-strings with special characters
special_char = "This is a tab:\tThis is a newline:\nThis is a backslash:\\"
print(f"Special characters:\n{special_char}")
#example 13: using f-strings with boolean values
is_student = True
print(f"Is Alice a student? {'Yes' if is_student else 'No'}")
#example 14: using f-strings with None
value = None
print(f"The value is: {value}")
#example 15: using f-strings with complex numbers
complex_num = 2 + 3j
print(f"The complex number is: {complex_num}, its real part is {complex_num.real} and imaginary part is {complex_num.imag}")
#example 16: using f-strings with lists and dictionaries
data = {"fruits": ["apple", "banana", "cherry"], "vegetables": ["carrot", "broccoli"]}
print(f"Fruits: {', '.join(data['fruits'])}")
print(f"Vegetables: {', '.join(data['vegetables'])}")

#example 17: using f-strings with custom objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age} years old"
person_obj = Person("David", 40)
print(f"Person details: {person_obj}")
