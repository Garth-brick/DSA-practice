from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:

    # we want to run binary search only on nums1, so lets make sure that its the smaller array
        if (len(nums2) < len(nums1)):
            # swap the two arrays if nums1 is larger than nums2 
            print("swapping")
            nums1, nums2 = nums2, nums1
        
        total_size = len(nums1) + len(nums2)
        half_size = (total_size) // 2

        l, r =0, len(nums1)-1

        while (True):
            mid1 = (l+r) // 2
            mid2 = half_size - mid1 - 1 - 1 # we deduct one 1 because mid1 is from a zero indexed array and another 1 because we want mid2 to refer to a ero-indexed array as well

            left1 = nums1[mid1] if (mid1 >= 0 and mid1 < len(nums1)) else float("-infinity") # if the nums1 array is empty then mid1 will become -1 and that would lead to a runtime error. So we if a value is inaccessible in our assumed left-half then we'll just take it to be -infinity so that it is lesser than whatever we get in our right-half and this value is practically ignored.
            left2 = nums2[mid2] if (mid2 >= 0 and mid2 < len(nums2)) else float("-infinity")

            right1 = nums1[mid1+1] if (mid1+1 < len(nums1) and mid1+1 >= 0) else float("infinity") # it is possible that there is no next element available in the array and we have already taken up all the elements, so in this case we put the right value as +infinity so that it is larger than whatever element we get in out left-half and this value is practically ignored.
            print(mid2, nums2)
            right2 = nums2[mid2+1] if (mid2+1 < len(nums2) and mid2+1 >= 0) else float("infinity")

            # we know that left1 is less than right1 because the array is sorted, so we just need to make sure that it is lesser than right2 before finalising our answer. Same for left2.
            if (left1 <= right2 and left2 <= right1):
                if (total_size % 2):
                    # total elements is odd
                    return min(right1, right2)
                else:
                    # total elements if even
                    # we want the average of the largest element in out left half and the smallest element in our right half
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif (left1 > right2):
                # if we have included too many elements from nums1
                r = mid1 - 1
            else:
                # if (left2 > right1)
                # we have included too few elements from nums1
                l = mid1 + 1

        return half_size # this line is actually not necessary at all but helf with typechecking, and besides, it feels like the half size should be a pretty common answer I guess

print(findMedianSortedArrays([1,3], [2]))