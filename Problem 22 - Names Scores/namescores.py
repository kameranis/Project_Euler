"""
Name Scores
Reads a file of names and after sorting computes the sum
of the numerical values times the position of the name
Konstantinos Ameranis 10.9.2013
"""

table = raw_input().split(",")
j=0
for i in table:
    table[j]=i.replace('"', '')
    j += 1
table.sort()
summ = 0
k = 1
for i in table:
    sub = 0
    for j in i:
        sub += ord(j)-ord("A")+1
    summ += sub*k
    k += 1
print summ
