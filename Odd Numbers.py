def print_odd_numbers(start, end):
    for i in range(start, end+1):
        if i % 2 != 0:
            print(i, end=' ')

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print("Odd numbers in the range:", end=' ')
print_odd_numbers(start, end)
