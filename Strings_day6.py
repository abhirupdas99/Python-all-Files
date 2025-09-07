#in python anything we enter in single or double quotes is considered as string
a='hello'
b="hello"
print(a)
print(b)
print(type(a))
print(type(b))

#multiline string using triple quotes
c='''hello
how are you'''
d="""hello
how are you"""
print(c)
print(d)

#string concatenation
e='hello'
f='world'
g=e+f
print(g)

#accessing string characters using indexing
h='hello'

for i in range(len(h)):
    print(h[i])

#negative indexing
for i in range(-1, -len(h)-1, -1):
    print(h[i])

#slicing strings
i='hello world'
print(i[0:5]) #hello
print(i[6:11]) #world
print(i[:5]) #hello
print(i[6:]) #world
print(i[:]) #hello world
print(i[::2]) #hlool
print(i[-2::2]) #el wrd
print(i[::-1]) #dlrow olleh 

# :: means step
# [start:end:step]  
#default start=0, end=len(string), step=1
#you can use negative step to reverse the string
print(i[-1::-2]) #dlrow olleh
print(i[-1:-len(i)-1:-1]) #dlrow olleh
print(i[-1:-6:-1]) #dlrow
print(i[-6::-1]) #dlrow olleh
print(i[-1:-len(i)-1:-2]) #dr olh
print(i[-1::-2]) #dr olh

#string methods
j=' hello world '
print(j.upper()) #HELLO WORLD
print(j.lower()) #hello world
print(j.strip()) #hello world                     #removes leading and trailing spaces
print(j.lstrip("l")) #hello world                    #removes leading l's
print(j.rstrip("d ")) # hello worl                #removes trailing d's and spaces
print(j.replace('h', 'H'))                        #Hello world #replaces h with H
print(j.split(' ')) #['', 'hello', 'world', '']   #splits the string at spaces
print(j.find('o')) #4                             #finds the first occurrence of o
print(j.count('o')) #2                            #counts the number of occurrences of o
print(j.startswith(' h')) #True                   #checks if string starts with ' h'
print(j.endswith('d ')) #True                     #checks if string ends with 'd '
print(j.isalpha()) #False                         #checks if all characters are alphabetic
print(j.isdigit()) #False                         #checks if all characters are digits
print(j.isspace()) #False                         #checks if all characters are whitespace
print(j.title()) # Hello World                     #capitalizes the first letter of each word
print(j.capitalize()) # Hello world                #capitalizes the first letter of the string
print(j.center(20, '*')) #**** hello world *****   #centers the string
print(j.zfill(20)) #0000000000 hello world 0000   #pads the string with zeros on the left to make it 20 characters long
print(j.encode()) #b' hello world '               #encodes the string to bytes
print(j.islower()) #True                          #checks if all characters are lowercase
print(j.isupper()) #False                         #checks if all characters are uppercase   
print(j.istitle()) #False                        #checks if the string is title cased
print(j.swapcase()) # HELLO WORLD                #swaps the case of each character
print(j.partition(' ')) #('', ' ', 'hello world ') #partitions the string at the first occurrence of ' '
print(j.rpartition(' ')) #(' hello world', ' ', '') #partitions the string at the last occurrence of ' '
print(j.rsplit(' ')) #['', 'hello', 'world', '']   #splits the string at spaces from the right
print(j.splitlines()) #[' hello world ']          #splits the string at line breaks
print(j.expandtabs()) # hello world               #expands tabs to spaces
print(j.removeprefix(' ')) #hello world           #removes the prefix ' ' if it exists
print(j.removesuffix(' ')) # hello world          #removes the suffix ' ' if it exists

