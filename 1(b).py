#write a python function to find all odd numbers up to a given n using a loop


def find_odd_numbers(n):
    odd_numbers = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers

# Example usage:
n = 100
print(find_odd_numbers(n))  # Output: [1, 3, 5, 7, 9]




