# recursion is a function that calls itself 

# Factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5 is:", factorial(5))

# Fibonacci series using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print("Fibonacci of 6 is:", fibonacci(6))

# Greatest Common Divisor (GCD) using recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print("GCD of 48 and 18 is:", gcd(48, 18))

# Sum of digits of a number using recursion
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
print("Sum of digits of 12345 is:", sum_of_digits(12345))

# Power of a number using recursion
def power(base,exp):
    if exp ==0:
        return 1
    else:
        return base*power(base,exp-1)
print("2 raised to the power 5 is:", power(2,5))
# Note: Always ensure that recursive functions have a base case to prevent infinite recursion.