#include <iostream>
#include <vector>
using namespace std;

int trap(vector<int>& height) {
    int trapped=0, l=0, r=(int)height.size()-1;
    int l_water_height = height[l];
    int r_water_height = height[r];
    while(l<r) {
        if (height[l] <= height[r]) {
            trapped += l_water_height - height[l];
            l++;
            l_water_height = max(l_water_height, height[l]);
        } else if (height[r] < height[l]) {
            trapped += r_water_height - height[r];
            r--;
            r_water_height = max(r_water_height, height[r]);
        }
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

/*2input
12
0 1 0 2 1 0 1 3 2 1 2 1
*/

/*input
6
4 2 0 3 2 5
*/