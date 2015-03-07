"""
Factorial digit sum
Computes the sum of the digits of nbr!
Konstantinos Ameranis 10.9.2013
"""

def factorial( n ):
    if n == 1:
        return 1
    return n * factorial( n - 1 )

nbr = input("Enter the number: ")
nbr = factorial(nbr)
summ = 0
while nbr:
    summ += nbr % 10
    nbr /= 10
print summ
