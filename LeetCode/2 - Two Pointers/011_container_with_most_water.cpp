#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxArea(vector<int>& height) {
    int l=0, r=(int)height.size()-1, max_area=0; 
    while(l<r) {
        int area = min(height[l], height[r]) * (r-l);
        max_area = max(area, max_area);
        if (height[l] < height[r]) {
            l++;
        } else {
            r--;
        }
    }
    return max_area;
}

int main() {
    int n;
    cin >> n;
    vector<int> input(n);
    for(int i=0; i<n; i++) {
        cin >> input[i];
    }
    cout << maxArea(input) << endl;
}

/*input
9
1 8 6 2 5 4 8 3 7 
*/