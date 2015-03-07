"""
Power Digit Sum
Computes the sum of the digits of the i power of 2
Konstantinos Ameranis 10.9.2013
"""

i=input()
summ=0
power=2**i
while power:
    summ+=power%10
    power/=10
print summ
