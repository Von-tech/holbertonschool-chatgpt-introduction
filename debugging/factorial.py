import sys

def factorial(n):
    if n < 0:
        print("factorial is not defined for negative numbers.")
        return None
    elif n == 0:
        return 1

result = 1
while n > 1:
    result *= n
    n -= 1
    return result

if len(sys.argv) != 2:
    print("Usage: ./factorial.py <number>")
else:
    try:
        f = factorial (int(sys.argv[1]))
        if f is not None:
            print(f)
    except ValueError:
        print("Please provide a valid integer.")
