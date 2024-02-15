print("1. Factorial Calculation\n2. Fibonacci Calculation\n4. Exit")
m=1
while(m>0):
    n = int(input("Select your choice: "))

    if n==1:
        fact=1
        num=int(input("Enter a number:"))
        for i in range(num, 0, -1):
            fact*=i
        print("The factorial of "+str(num)+" is: "+str(fact))

    elif n==2:
        a=0
        b=1
        num=int(input("Enter a number: "))
        print("The fibonacci of " + str(num) + " is: ")
        for i in range(num):
            print(b, end=" ")
            a, b = b, a+b

    else:
        break