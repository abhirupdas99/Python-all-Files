#passing function arguments
def add(x,y):
    return x + y
def calculate(func, a, b):
    return func(a, b)
result = calculate(add, 5, 3)
print("Result:", result)

#using *args and **kwargs
def display_info(*args, **kwargs):
    for arg in args:
        print("Arg:", arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(1, 2, 3, name="Alice", age=30)
display_info("Hello", "World", city="New York", country="USA")

#function annotations
def add(x: int, y: int) -> int:
    return x + y
print("Annotated add function:", add(10, 20))
print("Function annotations:", add.__annotations__)

