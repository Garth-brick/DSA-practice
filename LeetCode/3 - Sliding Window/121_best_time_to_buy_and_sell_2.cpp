#include <vector>
#include <iostream>
using namespace std;

// solved with O(1) memory and O(n) time

void print_vector(vector<int> vect) {
    cout << "[";
    for(int i=0; i<(int)vect.size()-1; i++) {
        cout << vect[i] << ", ";
    }
    cout << vect[vect.size()-1] << "]" << endl;
}

int maxProfit(vector<int>& prices) {
    int l=0, r=1, max_profit=0;
    while(r < (int)prices.size()) {
        if (prices[r] < prices[l]) {
            l = r;
        } else {
            max_profit = max(max_profit, prices[r] - prices[l]);
        }
        r++;
    }
    return max_profit;
}

int main() {
    int n;
    cin >> n;
    vector<int> input(n);
    for(int i=0; i<n; i++) {
        cin >> input[i];
    }
    cout << maxProfit(input);
}

/*input
6
7 1 5 3 6 4
*/