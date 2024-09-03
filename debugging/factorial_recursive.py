#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Function Description:
    This function computes the factorial of a given non-negative integer n using recursion.
    The factorial of n (denoted as n!) is the product of all positive integers less than or equal to n.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input integer n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the input argument and compute the factorial
f = factorial(int(sys.argv[1]))
print(f)

