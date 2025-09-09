#match case is a new feature in python 3.10 and later versions
#it is similar to switch case in other programming languages
choice= int(input("Enter a number between 1 and 5 "))
match choice:
    case 1:
        print("You chose 1")
    case 2:
        print("You chose 2")
    case 3:
        print("You chose 3")
    case 4:
        print("You chose 4")
    case 5:
        print("You chose 5")
    case _:
        print("Invalid choice")
#the underscore case is similar to the default case in switch case
#it will be executed if none of the above cases match

#you can also use match case with strings
day=input("Enter a day of the week: ")
match day.lower():
    case "monday":
        print("It's Monday")
    case "tuesday":
        print("It's Tuesday")
    case "wednesday":
        print("It's Wednesday")
    case "thursday":
        print("It's Thursday")
    case "friday":
        print("It's Friday")
    case "saturday":
        print("It's Saturday")
    case "sunday":
        print("It's Sunday")
    case _:
        print("Invalid day")