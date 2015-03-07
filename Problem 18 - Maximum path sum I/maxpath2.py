"""
Maximum path sum I
Finds the largest sum in a pyramid of numbers
Konstantinos Ameranis 18.9.2013
"""

N = 15
a = []
for i in range(N):
    a.append([int(num) for num in raw_input().split(' ')])
i = N-2
while i >= 0:
    for j in range(i+1):
        a[i][j] += max(a[i+1][j], a[i+1][j+1])
    i -=1
print a[0][0]
