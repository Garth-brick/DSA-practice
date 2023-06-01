#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
using namespace std;

bool compare(pair<int,int> lhs, pair<int,int> rhs) {
    return lhs.second < rhs.second;
}

int longest_consecutive(vector<int> nums) {
    unordered_set<int> s(nums.begin(), nums.end());
    unordered_map<int, int> mappy;
    for(int i : nums) {
        // if the number is the start of a sequence then put it into a hashmap
        if(s.count(i-1) == 0) {
            int num = i;
            mappy[i] = 1;
            while(s.count(++num) == 1) {
                mappy[i]++;
            }
        }
    }
    return max_element(mappy.begin(), mappy.end(), compare)->second;
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