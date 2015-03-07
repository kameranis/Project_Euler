"""Pandigital Products
Finds the sum of all pandigital products
Konstantinos Ameranis 2.12.2013
"""

def del_poss(i, a):
    for k in str(i):
        if not a[int(k)]:
            a[int(k)]=1
        else:
            return False
    return True

summ = 0
pan = []
for i in range(10000):
    for j in range(10000):
        k = i*j
        a = [0]*10
        a[0] = 1
        if not (del_poss(i, a) and del_poss(j, a) and del_poss(k, a)):
            continue
        b = True
        for l in a:
            b = b and l
        if b:
            pan.append(k)
            print i, j, k
pan = set(pan)
print pan
for i in pan:
    summ += i
print summ

