"""--------------------------------------------------------------------------------
The mathematician Srinivasa Ramanujan found an infinite series that can be used to
generate a numerical approximation of 1/π:

https://crypto.stanford.edu/pbc/notes/pi/ramanujan.html

Write a function called estimate_pi that uses this formula to compute and return an estimate of
π. It should use a while loop to compute terms of the summation until the last term is smaller than
1e-15 (which is Python notation for 10-15). You can check the result by comparing it to math.pi.

-------------------------------------------------------------------------------------"""

import math

def factorial(n):
    """Function to calculate factorial of n"""
    if n == 0:
        return 1
    return n*factorial(n-1)


def estimate_pi():
    "Function to estimate the value of pi using Ramanujan infinite series"
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        
        total += num / den
        term = factor * num/den
        
        if abs(term) < 1e-15:
            break
        k += 1
    
    return 1 / (factor * total)

print(estimate_pi())