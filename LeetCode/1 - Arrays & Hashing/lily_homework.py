#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#




def lilysHomework(arr):
    
    def minSwaps(arr):
        
        correct = sorted(arr)
        
        indexMap = {}
        
        for i, num in enumerate(arr):
            indexMap[num] = i
            
        swapCount = 0
        
        for i in range(len(arr)):
            if arr[i] != correct[i]:
                
                swapCount += 1
                
                swapIndex = indexMap[correct[i]]
                indexMap[arr[i]] = swapIndex
                arr[i], arr[swapIndex] = arr[swapIndex], arr[i]
        return swapCount
    
    rev_arr = arr[::-1]
    return min(minSwaps(arr), minSwaps(rev_arr))
    
        
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)
    
    print(result)
    
"""input
4
3 1 2 4
"""