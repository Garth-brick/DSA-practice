#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

// time O(n)
// space O(n)

int characterReplacement(string s, int k) {
    int result=0, max_freq=0, l=0, r=0; 
    // max_freq will track the number of times that the most frequent letter appears. It will kinda keep track of the key with the highest value withing the unordered map.
    unordered_map<int, int> mappy; // keep a map to track how many of each letter is there in the window
    while (r < (int)s.size()) {
        mappy[s[r]]++; // put the current right-pointer's letter into the map
        max_freq = max(max_freq, mappy[s[r]]); // reset the maximum frequency if needed
        int curr_length = r-l+1;
        if (curr_length > k + max_freq) {  // we can only make k replacements for a valid string, so if max_freq+k < curr_length then we won't be to change enough characters to create a valid string.
            mappy[s[l]]--; // drop the letter at the left pointer and increment the pointer
            l++;
        }
        result = max(result, r-l+1);
        r++;
    }
    return result;
}

int main() {
    int k;
    string str;
    cin >> k;
    getline(cin >> ws, str);
    cout << characterReplacement(str, k);
}

/*input
1
AABABBA
*/