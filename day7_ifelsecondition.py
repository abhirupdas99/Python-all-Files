#conditional statements in python
a=10
b=20
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater than a")

#nested if else
x=30
y=20
z=10
if x>y:
    if x>z:
        print("x is the greatest")
    else:
        print("z is the greatest")
else:
    if y>z:
        print("y is the greatest")
    else:
        print("z is the greatest")

