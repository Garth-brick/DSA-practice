#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>
using namespace std;

// THIS ONE JUST FAILS ON SOME BIG TEST CASE FOR SOME REASON!

int minEatingSpeed(vector<int>& piles, int h) {
    int piles_sum = accumulate(piles.begin(), piles.end(), 0);
    int l = piles_sum / h;
    cout << "l = " << l << endl;
    int r = *max_element(piles.begin(), piles.end()); // NOTE: the max_element function gives you a pointer to the maximum element, not the maximum element itself, you must deference it to get the element
    int result = r;
    while (l <= r) {
        int mid = l+(r-l)/2;
        long long hours_taken = 0;
        for (int pile : piles) {
            hours_taken += ceil((double)pile/mid);
        }
        if (hours_taken <= h) {
            result = mid;
            r = mid - 1;
        } else {
            l = mid + 1;
        }
    }
    return result;
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