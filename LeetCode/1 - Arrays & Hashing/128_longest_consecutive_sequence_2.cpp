#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
using namespace std;

int longest_consecutive(vector<int> nums) {
    unordered_set<int> s(nums.begin(), nums.end());
    int max_seq = 0;
    for(int i : s) {
        if(s.count(i-1) == 0) {
            int num = i;
            int cur_seq = 1;
            while (s.count(++num) == 1) {
                cur_seq++;
            }
            max_seq = max(max_seq, cur_seq);
        }
    }
    return max_seq;
}

int main() {
    int n;
    cin >> n;
    vector<int> vect(n);
    for (int i=0; i<n; i++) {
        cin >> vect[i];
    }
    cout << longest_consecutive(vect);
}

/*input
6
100 4 200 1 3 2
*/