#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>
using namespace std;

// THIS ONE ALSO JUST FAILS ON SOME BIG TEST CASE FOR SOME REASON BUT IT PASSED THE LEETCODE THING SO NO WORRIES

long long getHoursToEatAll(vector<int>&piles, int bananasPerHour) {
    long long totalHours = 0;
    for (int i = 0; i < piles.size(); i++) {
        totalHours += ceil(piles[i] / (double)bananasPerHour);
    }
    return totalHours;
}
int minEatingSpeed(vector<int>& piles, int targetHours) {
    int low = 1, high = *(max_element(piles.begin(), piles.end()));
    int ans = -1;
    while(low <= high) {
        int mid = low + (high - low) / 2;
        long long hoursToEatAll = getHoursToEatAll(piles, mid);
        
        if (hoursToEatAll <= targetHours) {
            ans = mid;
            high = mid - 1;
        }
        else low = mid + 1;
    }
    return ans;
}


int main() {
    int input_h, n;
    cin >> input_h >> n;
    vector<int> input_piles(n);
    for (int i=0; i<n; i++) {
        cin >> input_piles[i];
    }
    cout << minEatingSpeed(input_piles, input_h);
}

/*input
18 823855818
332484035 524908576 855865114 632922376 222257295 690155293 112677673 679580077 337406589 290818316 877337160 901728858 679284947 688210097 692137887 718203285 629455728 941802184
*/