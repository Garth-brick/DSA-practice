#include <iostream>
#include <vector>
using namespace std;


int search(vector<int>& nums, int target) {
    int l = 0;
    int r = (int)nums.size()-1;
    int result = -1;
    while (l <= r) {
        int mid = l + (r-l)/2;

        if (target == nums[mid]) {
            result = mid;
            break;
        }

        if (nums[l] <= nums[mid]) {
            // mid is in left-subarray
            if (target < nums[mid] && target >= nums[l]) {
                // if the target is present within the left-subarray itself
                r = mid-1;
            } else {
                l = mid + 1;
            }
        } else {
            // mid is right-subarray
            if (target > nums[mid] && target <= nums[r]) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
    }
    return result;
}


int main() {
    int input_target;
    cin >> input_target;
    int n;
    cin >> n;
    vector<int> input_nums(n);
    for (int i=0; i<n; i++) {
        cin >> input_nums[i];
    }
    cout << search(input_nums, input_target);
}

/*input
0
1
1
*/