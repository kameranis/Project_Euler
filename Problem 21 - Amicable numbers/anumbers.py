"""
Amicable numbers
Computes the sum of all amicable numbers under 10,000
Konstantinos Ameranis 18.9.2013
"""

s = 0
a = [0]
for i in range(1, 10000):
    subs = 0
    for j in range(1, i/2+1):
        if i % j == 0:
            subs += j
    a.append(subs)
    if subs < i:
        if i == a[subs]:
            s += i + subs
print s
