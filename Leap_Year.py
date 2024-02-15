year = int(input("Enter a Year: "))
leap = False

if year % 4 == 0:
    leap = True
    if year % 100 == 0:
        leap = False
        if year % 400 == 0:
            leap = True

print(leap)
