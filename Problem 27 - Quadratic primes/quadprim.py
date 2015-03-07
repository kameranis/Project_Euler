"""
Quadratic primes
Finds a*b where n^2 + a*n + b yields the most primes
Konstantinos Ameranis 21.11.2013
"""

def quad(n, a, b):
    return n*n + b*n + a

array=[0]*100000
array[0]=1
array[1]=1
for i in xrange(100000):
    if array[i]:
        continue
    for x in xrange(i, 100000/i):
        array[i*x]=1
maxi = 0
maxproduct = 0
for a in range (-999, 1000):
    for b in range(-999, 1000):
        n = -1
        product = 2
        while not array[product]:
            n += 1
            product = quad(n, a, b)
        if n > maxi:
            maxi = n
            maxproduct = a * b
print maxi, maxproduct

