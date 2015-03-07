"""
Lattice paths
Computes the possible lattice paths
Konstantinos Ameranis 15.11.2013
"""

def factorial( n ):
    if n == 1:
        return 1
    return n * factorial( n - 1 )

print factorial(40)/(factorial(20)**2)
