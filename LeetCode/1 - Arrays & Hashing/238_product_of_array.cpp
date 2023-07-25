#include <vector>
#include <iostream>
using namespace std;

void print_vector(vector<int> vect) {
    for(int i : vect) {
        cout << i << " ";
    }
    cout << endl;
}

vector<int> product_except_self(vector<int> &nums) {
    vector<int> output(nums.size(), 1);
    int x = 1; // x is for the running prefix
    for(int i=0; i< (int)nums.size(); i++) {
        output[i] = x;
        x *= nums[i];
    }
    x = 1; // x is now for the running postfix
    for(int i=nums.size()-1; i>=0; i--) {
        output[i] *= x;
        x *= nums[i];
    }
    return output;
}

int main() {
    int n;
    cin >> n;
    vector<int> nums;
    for (int i=0; i<n; i++) {
        int x;
        cin >> x;
        nums.push_back(x);
    }
    vector<int> output = product_except_self(nums);
    print_vector(output);
}

/*input
4
1 2 3 4
*/