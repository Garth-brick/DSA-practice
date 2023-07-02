from typing import List

""" NOTES 
- Note that the array is of size (n+1) and contains all numbers in the range [1..n] 
- We need to treat the values in this list as nodes of a list where the index of each element is its value as a node and the value of each element is the node that it will be pointing to. Basically, something like this:
    node.val = element.index
    node.next = element.val
- We need to find the head of the cycle because that's going to be the node that will have two nides pointing at it
    - Any value that ocurrs twice in the array will occupy two different indexes and will therefore be at the .next of two different nodes
    - We can now use Floyd's Fast and Slow pointer method to find the head of a cycle in a linked list 
"""

def findDuplicate(nums: List[int]) -> int:

    # detecting a cycle by starting a fast and slow pointer and making them traverse the list until they overlap
    slow: int = 0
    fast: int = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if (slow == fast):
            break
    
    # finding the head of the cycle by initialising another slow pointer at the head while the previously used fast and slow pointers are still at their overalapping position
    # then we this new slow pointer along with the old slow pointer until they both intersect
    # the place where these two slow pointers intersect now will be the head of linked list
    slow2: int = 0
    while True:
        slow2 = nums[slow2]
        slow = nums[slow]
        if (slow == slow2):
            return slow

print(findDuplicate([1,3,4,3,2]))