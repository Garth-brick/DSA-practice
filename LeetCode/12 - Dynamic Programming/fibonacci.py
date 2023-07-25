from typing import List
from timeit import timeit
import numpy as np


def fib(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
    
def fibWithMemo(n: int, memo: List[int]) -> int:
    if memo[n]:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibWithMemo(n-1, memo) + fibWithMemo(n-2, memo)
    memo[n] = result
    return result

def fibBottomUp(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    bottomUp = [0] * (n+1)
    # bottomUp = np.zeros(n+1, np.longdouble)
    bottomUp[1] = 1
    bottomUp[2] = 1
    for i in range(3, n + 1):
        bottomUp[i] = bottomUp[i-1] + bottomUp[i-2]
    return bottomUp[n]

def fibBottomUpTwoVariable(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    first = 1
    second = 1
    result = 1
    for _ in range(3, n+1):
        result = first + second
        second = first
        first = result
    return result
    
n = int(input())
print(timeit(lambda: fibBottomUp(n), number=1)) # using numpy actually makes this slower??? idk
print(timeit(lambda: fibBottomUpTwoVariable(n), number=1))

"""input
100000
"""