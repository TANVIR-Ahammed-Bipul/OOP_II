n=int(input("Enter a number: "))

if n>0:
    for i in range(n, -1, -1):
        print(i, end=" ")

elif n<0:
    for i in range(n, 1, +1):
        print(i, end=" ")

else:
    print(n)