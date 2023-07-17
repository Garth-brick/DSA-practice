from typing import List, Dict, Tuple

def findTargetSumWays(nums: List[int], target: int, i: int=0, memo: Dict[Tuple[int, int], int]=dict()) -> int:
    print(f"target = {target}")
    if i == len(nums):
        if target == 0:
            return 1
        return 0
    if (i, target) in memo:
        print(f"FOUND ({i},{target}) = {memo[(i, target)]}")
        return memo[(i, target)]
    
    num = nums[i]
    print(f"num = {num}")
    memo[(i, target)] = findTargetSumWays(nums, target-num, i+1, memo) + findTargetSumWays(nums, target+num, i+1, memo)
    print(f"--> returning memo[({i}, {target})] = {memo[(i, target)]}")
    return memo[(i, target)]

print(findTargetSumWays([1,0], 1))