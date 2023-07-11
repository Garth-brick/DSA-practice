import collections
from typing import List


""" NOTE
nums = [1,2,3]
- If we fix the first element as 1 as the first element then we now need find the permutations of [2,3]
- From this again if we fix 2 as the second element then we just need to find the permutation of [3]
- Since arrays of unit length can only have a single permutation, we can return it as is
"""


def permute(nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = []
    
    # base case: if there is only one element then it will have just one permutation
    if len(nums) == 1:
        return [nums.copy()]
    
    numsQ = collections.deque(nums)
    
    # removing each element, finding the permutations of the remaining elements, and adding it back into the queue once
    for _ in range(len(numsQ)):
        
        # remove the first element from the queue
        num: int = numsQ.popleft()
        
        # get the permutations of the ramining elements
        permutations: List[List[int]] = permute(list(numsQ))
        
        # add the removed number to each of the permutations to complete them
        for permutation in permutations:
            permutation.append(num)
            
            # add the permutations to the result once they are completed
            result.append(permutation)
        
        numsQ.append(num)
    
    return result

print(permute([1,2,3]))