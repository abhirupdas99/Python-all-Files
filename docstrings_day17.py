# docstrings in Python
# A docstring is a special type of comment that is used to describe the purpose and functionality of a module, class, method, or function.
# Docstrings are written using triple quotes (""" or ''') and are placed immediately after the definition of the module, class, method, or function.
# Docstrings can be accessed using the __doc__ attribute of the object. 
# They are also used by documentation generation tools to create documentation for the code.
# Example of a module docstring
"""This module provides functions for basic arithmetic operations."""
# Example of a function docstring
def add(a, b):
    """Returns the sum of two numbers a and b."""
    return a + b
def subtract(a, b):
    """Returns the difference of two numbers a and b."""
    return a - b
def multiply(a, b):
    """Returns the product of two numbers a and b."""
    return a * b
def divide(a, b):
    """Returns the quotient of two numbers a and b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
# Accessing docstrings
print("Module docstring:", __doc__)
print("add function docstring:", add.__doc__)
print("subtract function docstring:", subtract.__doc__)
print("multiply function docstring:", multiply.__doc__)
print("divide function docstring:", divide.__doc__)

#pep8 guidelines for docstrings
"""
1. Use triple double quotes for docstrings.
2. The docstring should start with a short description of the function's purpose.
3. If there are more details to add, include them after a blank line.
4. Use proper grammar and punctuation.
5. Include descriptions of parameters and return values if applicable.
6. Keep the docstring concise and to the point.
"""
# Example of a class docstring
class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""
    
    def add(self, a, b):
        """Returns the sum of two numbers a and b."""
        return a + b
    
    def subtract(self, a, b):
        """Returns the difference of two numbers a and b."""
        return a - b
    
    def multiply(self, a, b):
        """Returns the product of two numbers a and b."""
        return a * b
    
    def divide(self, a, b):
        """Returns the quotient of two numbers a and b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
# Accessing class and method docstrings
print("Calculator class docstring:", Calculator.__doc__)
print("Calculator add method docstring:", Calculator.add.__doc__)
print("Calculator subtract method docstring:", Calculator.subtract.__doc__)
print("Calculator multiply method docstring:", Calculator.multiply.__doc__)
print("Calculator divide method docstring:", Calculator.divide.__doc__)
# Example of a method docstring with parameters and return value description
class AdvancedCalculator:
    """An advanced calculator class to perform additional arithmetic operations."""
    
    def power(self, base, exponent):
        """
        Returns the result of raising base to the power of exponent.
        
        Parameters:
        base (float): The base number.
        exponent (float): The exponent to raise the base to.
        
        Returns:
        float: The result of base raised to the power of exponent.
        """
        return base ** exponent 
# Accessing method docstring
print("AdvancedCalculator power method docstring:", AdvancedCalculator.power.__doc__)
# Docstrings are an essential part of writing clean and maintainable code in Python. They help other developers (and your future self) understand the purpose and functionality of your code.
# Always include docstrings in your modules, classes, methods, and functions to improve code readability and usability.
