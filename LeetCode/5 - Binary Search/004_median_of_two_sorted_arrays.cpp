#include <iostream>
#include <vector>
#include <climits>
#include <cmath>
using namespace std;


/* THINKING
- A number is the median in a sorted array if there are an equal number of elements to its left and right
- If there is an even number of elements then we need to find an element with n elements to its left, and n+1 elements to its right, then take the average of that element and the element right after it.
- Neetcode:
    - Compute how many elements you need on one half (just add the sizes of both the arrays and divide by two)
    - Start a left and a right pointer in the first array, calculate the middle (assume that all the elements in your array uptil the middle value are in your left half)
    - If you still need more elements for your left half then take them from the second array
    - After getting enough elements from your left half, check if the partition is valid 
        - Every element in the left half must be lesser than every element in the right half
        - Since the arrays are sorted, if the right-most element in each left-half is lesser then the left-most element in the other array's right-half then we have correctly found the left-half.
    - If one of the elements in the left half is smaller than one of the elements in the right-half then shift the left pointer so that the next middle element has a larger right-most element

- Optimisation: Since we only have to run binary search on one of these arrays, it is beneficial to run it on the smaller array 
*/

//  SEE MORE NOTES IN THE PYTHON VERSION

double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

    // since we are only doing a binary search on nums1 lets make sure its the smaller array
    if (nums1.size() > nums2.size()) {
        swap(nums1, nums2);
    }

    int l=0, r=(int)nums1.size()-1;
    int total_size = (int)nums1.size() + (int)nums2.size();
    int half_size = total_size / 2;

    while (true) {
        int mid1 = (int)floor((float)(l+r)/2); // flooring the value here is really important to be able to handle -ve values
        int mid2 = half_size - mid1 - 1 - 1;

        int left1 = (mid1 >= 0 && mid1 < (int)nums1.size()) ? nums1[mid1] : INT_MIN;
        int left2 = (mid2 >= 0 && mid2 < (int)nums2.size()) ? nums2[mid2] : INT_MIN;
        int right1 = (mid1+1 >= 0 && mid1+1 < (int)nums1.size()) ? nums1[mid1+1] : INT_MAX;
        int right2 = (mid2+1 >= 0 && mid2+1 < (int)nums2.size()) ? nums2[mid2+1] : INT_MAX;

        if (left1 <= right2 && left2 <= right1) {
            if (total_size % 2) {
                // if total_size is odd
                return min(right1, right2);
            } else {
                // if total_size is even
                return (double)(max(left1, left2) + min(right1, right2)) / 2;
            }
        } else if (left1 > right2) {
            // we have taken too many elements from nums1
            r = mid1 - 1;
        } else {
            // if (left2 > right1) then we have taken too few elements from num1
            l = mid1 + 1;
        }
    }
}


int main() {
    vector<int> input_nums1 = {1,3};
    vector<int> input_nums2 = {2};
    cout << findMedianSortedArrays(input_nums1, input_nums2);
}
