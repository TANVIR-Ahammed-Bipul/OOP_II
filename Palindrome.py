def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a number: ")
if is_palindrome(word):
    print("Palindrome!")
else:
    print("Not a palindrome.")
