import math

input_number = int(input("Enter a number to check if it is a Perfect Square: "))

def is_perfect_square(n):
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

if is_perfect_square(input_number):
    print(f"{input_number} is a perfect square.")
else:
    print(f"{input_number} is not a perfect square.")