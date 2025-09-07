#typecasting in python
a=5
b=2.5
c="10"
d="20.5"
print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#typecasting
a=float(a)
b=float(b)
c=int(c)
d=float(d)
print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# implicit typecasting vs explicit typecasting
x=5
y=2.5
z=x+y #implicit typecasting
print(z)
print(type(z))

x=5
y=2.5
z=int(x)+int(y) #explicit typecasting
print(z)
print(type(z))

#implicit typecasting are those which are done by python automatically
#explicit typecasting are those which are done by user manually
#you cant convert string to int or float if it contains non-numeric values
s="hello"
#s=int(s) #error    
