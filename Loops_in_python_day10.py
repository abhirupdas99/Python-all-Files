#Loops in Python
#Python has two primitive loop commands:
#1. while loops
#2. for loops

#1. while loops
#A while loop is used to execute a block of code repeatedly as long as a given condition is true.
#The syntax for a while loop is as follows:

while condition:
    # code to be executed

#example of a while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # this is equivalent to count = count + 1
    print("Loop ended")
    print("Final count is:", count)


#2. for loops
#A for loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or other iterable objects.
#The syntax for a for loop is as follows:
for item in sequence:
    # code to be executed

#Here, 'item' is a variable that takes the value of each element in the sequence one by one, and the loop continues until all elements have been processed.

#example of a for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit is:", fruit)
    print("Loop ended")
    print("All fruits have been printed.")


#do-while loop
#Python does not have a built-in do-while loop like some other programming languages.
#However, you can simulate a do-while loop using a while loop with a break statement
#example of simulating a do-while loop
count = 0
while True:
    print("Count is:", count)
    count += 1
    if count >= 5:
        break   # exit the loop when count is 5 or more
print("Final count is:", count)
print("Loop ended")
print("All counts have been printed.")
#Note: Be careful with while loops to avoid infinite loops, which occur when the condition never becomes false. Always ensure that the loop has a way to terminate.
#You can use the break and continue statements to control the flow of loops
#break statement is used to exit the loop prematurely