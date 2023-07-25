""" NOTES
nums = [2,3,6,7]
target = 7
expected output = [[2,2,3], [7]]

NAIVE APPROACH
- Have four branches from the root of the decision tree, one where you take 2, one where you take 3, one with 6, and one with 7.
- From each of them, have 4 more branches so that you can cover all four possibility again until the sum reaches the target. Add the combination to the result whenever the sum reaches the target
- But this will lead to DUPLICATE combinations! They might be a different permuation but we'll get the same combination multiple times such as [2,3] and [3,2] will be along different branches of our decision tree and get treated as different which we want to avoid

FIRST APPROACH
- Make two branches from the root node, one which includes atleast one two and another which doesn't have any 2s
- From the branch with atleast one 2, make two more branches - one with atleast two 2s and one with only one 2.
- After you have reached the number of 2s desired for a given branch, create two branches for choosing or not choosing the numbers as well
- If the sum equals the target then add to the result
- Do this until the sum exceeds the target then stop the branch
"""

from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    
    result = []
    
    def dfs(i: int, combination: List[int], sum) -> None:
        if sum > target or i >= len(candidates):
            return
        
        if sum == target:
            result.append(combination.copy())
            return
        
        num = candidates[i]

        # including num and not incrementing i to see if it should be included again
        dfs(i, combination + [num], sum + num)
        
        # not including num but incrementing i so that we can check if the next number should be added instead
        dfs(i+1, combination, sum)
        
    dfs(0, [], 0)
    return result

print(combinationSum([2,3,6,7], 7))