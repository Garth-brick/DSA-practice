#include <vector>
#include <iostream>
using namespace std;

// solved by storing the highest future price for every point

void print_vector(vector<int> vect) {
    cout << "[";
    for(int i=0; i<(int)vect.size()-1; i++) {
        cout << vect[i] << ", ";
    }
    cout << vect[vect.size()-1] << "]" << endl;
}

int maxProfit(vector<int>& prices) {
    int n=(int)prices.size(), max_profit=0;
    vector<int> profit(n, 0);

    // store the highest price in the future of every point
    int mp = prices[n-1];
    for(int i=n-1; i>=0; i--) {
        mp = max(mp, prices[i]);
        profit[i] = mp;
    }

    // subtract the lowest price in the past of each point
    mp = prices[0];
    for(int i=0; i<n; i++) {
        mp = min(mp, prices[i]);
        max_profit = max(max_profit, profit[i]-mp);
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
7 6 4 3 2 1
*/