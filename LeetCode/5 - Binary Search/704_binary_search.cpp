#include <iostream>
#include <vector>
using namespace std;


int search(vector<int>& nums, int target) {
    int l=0, r=nums.size()-1;
    while (l <= r) {
        int mid = (r+l)/2;
        if (nums[mid] < target) {
            l=mid+1;
        }
        else if (nums[mid] > target) {
            r = mid-1;
        } 
        else {
            return mid;
        }
    }
    return -1;
}


int main() {
    vector<int> input_nums = {5};
    int target = 5;
    cout << search(input_nums, target);
}