"""
Special Pythagorean Triplet
Computes the product a*b*c of the pythagorean triplet with a + b + c = 1000
Konstantinos Ameranis 18.9.2013
"""

import math

a = 1
b = 2
c = 1000 - a - b
while a < 1000 / 3 and a*a + b*b != c*c:
    while c > 0 and a*a + b*b != c*c:
        b += 1
        c = 1000 - a - b
    if a*a + b*b == c*c:
        break
    a += 1
    b = a+1
    c = 1000 - a - b
print "Success:", a * b * c
