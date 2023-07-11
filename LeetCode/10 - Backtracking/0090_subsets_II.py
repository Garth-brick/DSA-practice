from typing import List


""" NOTE
nums = [1,2,2,3]
- At every point in the decision tree we have two branches (one that includes a number and one that doesn't include a number)
- The standard strategy for creating subsets fails here because if we chose to include the first 2 in one branch and not in the other then the other branch could still go on to get that second two!
            
               1
             /   \\       left side includes the number at index 1, right side doesn't #
            /     \\      nums[1] = 2
         1 2        1
        / \\       / \\    left side includes the number at index 2, right side doesn't
       /   \\     /   \\   nums[2] = 2
     ..  [1 2] [1 2]   ..
           ^     ^
          duplicates  
          
- SOLUTION: If you include 2s in one branch and don't include any 2s in the other branch then there will be no duplicates.G
"""


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
        # keeping a globally accessible result set
        resultSet: List[List[int]] = []

        # ensure that the nums array is sorted so that we can easily skip over groups of duplicates
        nums.sort()

        def dfs(i, subset):
            
            # if we have gone through all the numbers then add the resultant subset to the result
            if i >= len(nums):
                resultSet.append(subset.copy())
                return
            
            # If we choose to include the current number
            dfs(i+1, subset + [nums[i]])

            # this is the branch which shouldn't have any 2s 
            # we need to increment i until we reach the next unique number (or the end of nums)
            if i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1, subset)

        dfs(0, [])
        return list(resultSet)
    
print(subsetsWithDup([1,2,2,3]))