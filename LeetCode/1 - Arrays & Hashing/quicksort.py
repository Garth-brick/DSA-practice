""" NOTE
- This is a divide and conquer algorithm
- Breaks a larger problem into multiple subprolems until the subproblems are simple to solve
- Solutions of the subproblems get combined to form the solution of the original problem
- time: O(n^2) in the worst case
        O(n * log(n)) in the best and average cases
- This sorts the elements in place so it doesn't require any additional memory
- General method:
    1. Choose a pivot element
    2. Put all elements less than the pivot in the left subarray and all elements greater than the pivot in the right subarray
    3. Call quicksort on the left subarray and on the right subarray
    4. If an array is of size=1 then it is sorted
    
- For every iteration:
    1. Keep the pivot pointer (p) at the last element
    2. Keep a left pointer (l) at the first element and a right pointer (r) at the second last element --> l will continuosly look for an element greater than the pivot and r will look for an element smaller than the pivot so that the two can be swapped when needed.
    3. If arr[l] < arr[p] then: increment l
    4. If arr[l] < arr[p] then:
        A. if arr[r] < arr[p] then: swap arr[l] with arr[r] and increment l
        B. if arr[r] >= arr[p] then: decrement r until condition-A becomes true
    5. If r <= l then: break the loop, move the pivot to the current position of l. 
"""


from typing import List


def partition(arr, left, right) -> int:
    l = left
    r = right - 1
    pivot = arr[right]
    
    while l < r:
        while l < right and arr[l] < pivot:
            l += 1
        while r > left and arr[r] >= pivot:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
    if arr[l] > pivot:
        arr[l], arr[right] = arr[right], arr[l]
    
    return l


# 'right' is the index of the last element
def quicksort(arr: List[int], left: int, right: int) -> None:
    if left < right:
        partition_position = partition(arr, left, right)
        quicksort(arr, left, partition_position-1)
        quicksort(arr, partition_position+1, right)
            

arr = [2, 6, 5, 1, 7, 4, 3]
quicksort(arr, 0, len(arr)-1)
print(arr)