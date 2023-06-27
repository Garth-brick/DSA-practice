import math
from typing import List

"""
We will definitely be able to eat all bananas if our speed is equal to teh max number of bananas in a pile therefore:
    sum(piles) <= min_eating_speed <= max(piles)
Instead of trying every value from 1..max_pile we can instead perform a binary search within those constraints
"""


def minEatingSpeed(piles: List[int], h: int) -> int:
    # get the upper bound for the binary search
    r = max(piles)
    l = math.ceil(sum(piles)/h)
    result = r
    while l <= r:
        mid = (l+r)//2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/mid)
        
        if hours <= h:
            result = min(result, mid)
            r = mid - 1
        else:
            l = mid + 1

    return result



# then we take in all the numbers for the list in one line
piles = list(map(int, input().strip().split()))
# input() will always give us a string
# strip() removes whitespace from the start and the end of the input
# split() creates a list by using " " as a delimeter between elements
# map() applies the int() function to each element in the list of strings
# [:n] limits the list to n elements even if more were given as input

h = int(input())

print(minEatingSpeed(piles, h))

"""input
30 11 23 4 20
5
"""