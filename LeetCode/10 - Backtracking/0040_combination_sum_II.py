from typing import List

""" NOTE
- combine the concepts learned in 'subsets-II' and in 'combination sum'
"""


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    result: List[List[int]] = []
    
    candidates.sort()
    
    def dfs(i: int, subset: List[int], sum: int) -> None:
        if sum == target:
            result.append(subset.copy())
            return
        
        if sum > target or i >= len(candidates):
            return
        
        dfs(i+1, subset + [candidates[i]], sum + candidates[i])
        
        while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
            i += 1
        dfs(i+1, subset, sum)
            
        
    dfs(0, [], 0)
    
    return result

print(combinationSum2([10,1,2,7,6,1,5], 8))