box=5
print("Please guess a number from 1 to 9: ")
starting_num=1
guess_limit=3
while(starting_num<=guess_limit):
    guess=int(input("Enter a number: "))
    starting_num+=1
    if guess==box:
        print("O yeah, Number found!")
        break

else:
    print("O sorry number not found! Try again.")