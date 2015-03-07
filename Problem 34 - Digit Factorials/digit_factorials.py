"""
Digit Factorials Euler Problem 34
The sum of the factorials of the digits is equal to the number itself
Konstantinos Ameranis 27/1/2015
"""

import math
import numpy as np

fact = np.array(map(math.factorial, range(10)))

def main(number):
    facts = map(lambda x: sum(fact[map(int, str(x))]), np.arange(10, number))
    print sum(np.arange(10, number)[np.where([facts[i-10] == i for i in np.arange(10, number)])])

if __name__ == '__main__':
    main(1000000)

