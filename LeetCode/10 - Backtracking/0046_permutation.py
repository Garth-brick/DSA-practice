""" NOTE

MY THOUGHT
- We can have a chosen set and remaining set and we can make a decision tree where we keep moving different values from our chosen set to the remainging set

FIRST APPROACH
- keep a global result variable
- 
"""

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = []
    
    def dfs(path: List[int], used: List[int]) -> None:
        
        if len(path) == len(nums):
            result.append(path.copy())
            return
        
        for i, num in enumerate(nums):
            
            # checking if the number has already been included
            # move to the the next number if this one is already used
            if used[i]:
                continue
            
            # add the number to the permutaion
            path.append(num)
            used[i] = True
            dfs(path, used)
            
            # remove the number for the permutation
            path.pop()
            used[i] = False
        
    dfs([], [False] * len(nums))
    return result

print(permute([1,2,3]))