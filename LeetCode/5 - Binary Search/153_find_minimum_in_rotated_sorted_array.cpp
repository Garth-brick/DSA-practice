#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;


// The rotated sorted array will always have two halves which are sorted properly within themselves
// If our middle value is in the left-sorted-part then we want go to the rightsorted-part because the right-sorted-part will always be the one with the smallest value present


int findMin(vector<int>& nums) {
    int l=0, r=(int)nums.size()-1;
    int result = INT_MAX;
    while (l<=r) {

        if (nums[l] < nums[r]) {
            // if we already have a sorted array in our window then return the leftmost element
            return min(result, nums[l]);
        }

        // finding the middle index while avoiding an overflow
        int mid = l + (r-l)/2;

        // maybe the mid value is the minimum only, so assign it the result straight up before changing the pointers
        result = min(result, nums[mid]);

        if (nums[mid] >= nums[l]) {
            // if we are in the left-sorted-part then we want to get to the left-sorted-part
            l = mid + 1;
        } else {
            // if we are in the right-sorted-part then we want to find the left-most value in this right-sorted-part
            
            r = mid - 1;
        }
    }
    return result;
}


int main() {
    int n;
    cin >> n;
    vector<int> input_arr(n);
    for (int i=0; i<n; i++) {
        cin >> input_arr[i];
    }
    cout << findMin(input_arr);
}

/*input
5
4 5 1 2 3
*/