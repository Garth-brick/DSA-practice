from typing import List


""" NOTE
- We will go over the nums array while choosing to either include or not include each element from nums in each subset variant
- Use a global result variable to store all the subsets
"""


def subsets(nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = []
    
    def dfs(i : int, subset: List[int]):
        if not i < len(nums):
            result.append(subset)
            return
        
        # calling dfs without including nums[i]
        dfs(i+1, subset)
        
        # calling dfs with nums[i] in the subset
        # the '+' creates a new list and passes that as the argument
        dfs(i+1, subset+[nums[i]]) 
        
        # we don't need the subset variable anymore
        del subset
        
    dfs(0, [])
    
    return result

print(subsets([1,2,3]))

"""
nums = [1,2,3]

dfs(0, [])
│
├── (1, [])
│   ├── (2, [])
│   │   ├── (3, [])
│   │   └── (3, [3])
│   └── (2, [2])
│       ├── (3, [2])
│       └── (3, [2,3])
└── (1, [1])
    ├── (2, [1])
    │   ├── (3, [1])
    │   └── (3, [1,3])
    └── (2, [1,2])
        ├── (3, [1,2])
        └── (3, [1,2,3])
"""