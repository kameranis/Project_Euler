"""
Counting Sundays
Counts the sundays of the 1st of the month in the 20th century
Konstantinos Ameranis 25.11.2013
"""

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = 365
count = 0
for y in range(1901, 2001):
    for d in days:
        if date % 7 == 6:
            count += 1
        date += d
        if d== 28 and y % 4 == 0:
            date += 1
print count
