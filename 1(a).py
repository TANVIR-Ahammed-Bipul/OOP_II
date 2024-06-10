# write a python function that checks if a given string is a palindrome (read the same forward and backwards)




n = input("Enter string : ")

h = n[::-1]
if n == h:
    print("palindrome")
else:
    print("Not palindrome")