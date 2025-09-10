print("Welcome to KBC")
mylist=[["Which is the smallest ocean in the world?","Arctic Ocean","Indian Ocean","Atlantic Ocean","Pacific Ocean",1],
        ["Which is the largest continent in the world?","Africa","Asia","Europe","Australia",2],
        ["Which is the largest country in the world?","India","USA","Russia","China",3],
        ["Which is the largest desert in the world?","Sahara","Thar","Gobi","Kalahari",1],
        ["Which is the longest river in the world?","Nile","Amazon","Yangtze","Mississippi",1]]
cash=0
for i in range(len(mylist)):
    print(mylist[i][0])
    for j in range(1,5):
        print(j,".",mylist[i][j])
    while True:  # Keep asking until valid input is provided
            print("Enter your Answer")
            inp=input()
            try:
                if mylist[i].index(inp)==mylist[i][5]:
                    cash=cash+10000
                    print("Your answer is correct. Congratulations! You have won",cash)
                    break  # Exit the while loop and go to next question
                else:
                    print("Sorry,Your answer is wrong. You have won",cash,". Better luck next time!")
                    print("Thank you for playing KBC")
                    exit()  # Exit the entire program
            except ValueError:
                print("Invalid input. Please enter a valid option from the given choices.")
print("Thank you for playing KBC")