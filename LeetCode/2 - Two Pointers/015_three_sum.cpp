#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void print_vector(vector<int> v) {
    cout << "[";
    for (int i=0; i<(int)v.size()-1; i++) {
        cout << v[i] << ", ";
    }
    cout << v[v.size()-1] << "]" << endl;
}

vector<vector<int>> three_sum(vector<int>& nums) {
    vector<vector<int>> output;
    // first sort the vector and then go over each element, doing two-sum on the remaining elements to find two other numbers such that they form a triplet with the chosen number
    sort(nums.begin(), nums.end());
    for (int i=0; i<(int)nums.size(); i++) {
        // if a number appears twice in the sorted array then skip over it
        if(i>=1 && nums[i] == nums[i-1]) {
            continue;
        }

        // perform two-sum on the remaining numbers
        int l=i+1, r=(int)nums.size()-1;
        int target = -1 * nums[i];
        while(l<r) {
            int sum = nums[l] + nums[r];
            if (sum < target) {
                l++;
            } else if (sum > target) {
                r--;
            } else {
                vector<int> triplet = {nums[i], nums[l], nums[r]};
                output.push_back(triplet);

                // we also need to move the left pointer to the next unique digit to avoid duplicates --> once the left pointer changes, the right pointer will automatically move given our two-pointer logic above
                while(l<r && nums[l]==triplet[1]) {
                    l++;
                }
            }
        }
    }
    return output;
}

void print(vector<vector<int>> vect) {
    cout << "[";
    for (vector<int> v : vect) {
        cout << "[";
        for (int i=0; i<(int)v.size()-1; i++) {
            cout << v[i] << ", ";
        }
        cout << v[v.size()-1] << "]";
    }
    cout << "]" << endl;
}

int main() {
    int n;
    cin >> n;
    vector<int> input(n);
    for (int i=0; i<n; i++) {
        cin >> input[i];
    }
    print(three_sum(input));
    return 0;
}

/*input
6
-1 0 1 2 -1 -4
*/