"""
Number letter counts
Sums the letters needed to write all numbers in [1, LIMIT]
Konstantinos Ameranis 18.9.2013
"""

LIMIT = 1000

small = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 9, 8]
big = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
hundred = 7
nd = 3
s = 900 * hundred + 890 * nd
for i in range(10):
    s += 190 * small[i]
    s += 10 * small[i+10]
    s += 100 * big[i]
print s + 4
