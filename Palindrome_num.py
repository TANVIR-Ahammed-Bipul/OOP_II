num=int(input("Enter a number: "))
n=num
rev=0

while (num>0):
    flag= num%10
    rev=rev*10+flag
    num=num//10

if(n==rev):
    print("The number is Palindrome")

else:
    print("Number is not Palindrome")