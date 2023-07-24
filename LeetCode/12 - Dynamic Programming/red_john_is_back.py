import math
import os
import random
import re
import sys
from typing import Dict, List

# JUST DOESN'T WORK FOR SOME REASON

def primes(n: int):
    # returns the number of prime numbers before n
    # uses the sieve of eratasthones
    # True denotes that a number is assumed to be prime
    primes: List[bool] = [True] * n
    primes[0] = False
    primes[1] = False
    for i in range(2, math.isqrt(n)+1):
        if primes[i]:
            # if this number is a prime then mark all of its multiples as non-prime
            for x in range(i*i, n, i):
                primes[x] = False
    return primes.count(True)
    
def find_confings(n: int, memo: Dict[int, int]=dict()):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif n in memo:
        return memo[n]
    result = find_confings(n-1, memo) + find_confings(n-4, memo)
    memo[n] = result
    return result

def redJohn(n):
    return primes(find_confings(n+1))

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = redJohn(n)

        print(str(result))
        

print(find_confings(11+1))
print(primes(26))

"""input
1
10
"""