"""
Highly Divisible Triangular Number
Finds the first triangular number which has over 500 divisors
Konstantinos Ameranis 13.9.2013
"""

import math

def highdiv(y, x):
    count = 0
    for i in range(1, int(math.sqrt(x))):
        if x % i ==0:
            count += 2
    if x % int(math.sqrt(x)) == 0:
        count += 1
    if count > 500:
        return False
    else:
        return True

summ = 1
i = 1
while highdiv(i, summ):
    i += 1
    summ += i
print summ
