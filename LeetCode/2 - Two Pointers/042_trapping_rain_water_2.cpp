#include <iostream>
#include <vector>
using namespace std;

// APPARENTLY this isn't a lot faster than the previous solution that I came up with

void print_vector(vector<int> v) {
    cout << "[";
    for (int i=0; i<(int)v.size()-1; i++) {
        cout << v[i] << ", ";
    }
    cout << v[v.size()-1] << "]" << endl;
}

int trap(vector<int>& height) {
    int trapped=0, n=height.size();
    vector<int> max_left(n,0), max_right(n,0);

    // create a vector which stores the maximum height to the left of each index
    int ml=0;
    for (int i=0; i<n; i++) {
        max_left[i] = ml;
        ml = max(ml, height[i]);
    }

    // same for storing the maximum height to the right of each index
    int mr=0;
    for (int i=n-1; i>=0; i--) {
        max_right[i] = mr;
        mr = max(mr, height[i]);
    }

    // go over the array once again and if the height at any index is less than the min of max_left and max_right at that index then trap water in that index
    for (int i=0; i<n; i++) {
        int water_height = min(max_left[i], max_right[i]);
        trapped += max(0, water_height - height[i]);
    }

    return trapped;
}

int main() {
    int n;
    cin >> n;
    vector<int> input(n);
    for(int i=0; i<n; i++) {
        cin >> input[i];
    }
    cout << trap(input);
}

/*input
12
0 1 0 2 1 0 1 3 2 1 2 1
*/

/*2input
6
4 2 0 3 2 5
*/