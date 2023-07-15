from typing import List

# we will do a binary search for the target but if it doesn't exist then we will return the element just greater than it
# if the target is greater than the gretest element then we return the index of the greatest element in the array 
def nearestGreaterElementIndex(nums: List[int], target: int):
    nums.sort()
    l = 0
    r = len(nums) - 1
    result = r
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            result = mid
            break
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
            result = mid
    return result

print(nearestGreaterElementIndex([1,2,5], 3))