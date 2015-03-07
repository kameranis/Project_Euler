"""
1000-digit Fibonacci Number
Computes the first 1000-digit Fibonacci Number
Konstantinos Ameranis 10.9.2013
"""

old = 1
current = 1
number = 2
new = 0
p = 10**999
while new <= p:
    new = old + current
    old = current
    current = new
    number += 1
print number
