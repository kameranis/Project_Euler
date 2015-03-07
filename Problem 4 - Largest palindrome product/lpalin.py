"""
Largest Palindrome Product
Finds the largest palindrome which is the product of 2 3-digit numbers
Konstantinos Ameranis
"""

def makepalin(i):
    x = i*1000+int(str(i)[::-1])
    for j in range(999, 100, -1):
        if (x % j == 0) and (x/j < 1000):
            print "The number you seek is:", x
            return True
    return False

flag = False
i = 998
while i > 99 and not flag:
    flag = makepalin(i)
    i -= 1
