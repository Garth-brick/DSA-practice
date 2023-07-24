""" NOTE
- This is a divide and conquer algorithm which means that we try to break a large problem into multiple subproblems recursively until each subproblem becomes simple to solve. We then combine the results of the suboroblems to solve the original larger subproblem.
- time: O(n * log(n))
- This is the optimal time complexity for comparison based sorting algorithm
- General method:
    1. Split the array in half until we have an array of size=1
    2. Call mergesort on each array
    3. Merge the sorted halves into one sorted array 
"""

def mergesort(arr):
    if len(arr) <= 1:
        # an array of size 1 is always sorted
        return
    
    # splitting the array
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    mergesort(left)
    mergesort(right)
    
    # merging time
    # assume that arr_l and arr_r have been sorted individually
    i_left = 0
    i_right = 0
    i_merged = 0
    while i_left < len(left) and i_right < len(right):
        if left[i_left] < right[i_right]:
            arr[i_merged] = left[i_left]
            i_left += 1
        else:
            arr[i_merged] = right[i_right]
            i_right += 1
            
        i_merged += 1
        
    # leftover elements in the left array
    while i_left < len(left):
        arr[i_merged] = left[i_left]
        i_left += 1
        i_merged += 1
        
    # leftover elements in the right array
    while i_right < len(right):
        arr[i_merged] = right[i_right]
        i_right += 1
        i_merged += 1
    
arr = [2, 6, 5, 1 , 7, 4, 3]
mergesort(arr)
print(arr)