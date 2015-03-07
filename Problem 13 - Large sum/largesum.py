"""
Project Euler Problem 13 - Large Sum
Sums 100 50-digit numbers and prints the first 10 digits
Konstantinos Ameranis 9.9.2013
"""

sum=0
for i in range(0, 100):
    x=input()
    sum=sum+x
print sum/10**42
