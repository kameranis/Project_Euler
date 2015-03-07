"""
Non abundant sums
Computes the sum of all the numbers that cannot be
expressed as the sum of two abundant numbers
Konstantinos Ameranis 31.10.2013
"""

def divsum(x):
    "Computes the sum of the divisors of x"
    s = 0
    for i in range (1, x/2+1):
        if x % i == 0:
            s += i
    return s

def issa(x, mlist):
    "Checks if x can be written as a sum of 2 abundant numbers"
    for i in range(len(mlist)/2):
        if x-mlist[i] in mlist:
            return False
    return True

s = 55
mlist = []
for i in xrange(11, 28123):
    if i < divsum(i):
        mlist.append(i)
    if issa(i, mlist):
        s += i
print s
