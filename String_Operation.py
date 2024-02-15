print("1. UpperCase\n2. Find String")

while True:
    n=int(input("Enter your Choice: "))
    if n==1:
        name=input("Enter name: ")
        print(name.upper())

    elif n==2:
        find_str="Tanvir Ahammed Bipul"
        looking=input("Enter the character: ")
        print(find_str.find(looking))

    else:
        break