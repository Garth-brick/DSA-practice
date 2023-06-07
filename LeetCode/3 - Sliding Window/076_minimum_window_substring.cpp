#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;


// solution is correct but exceeds the time limit


string minWindow(string s, string t) {
    string result="", curr="";
    unordered_map<char, int> mp1, mp2;
    for (char c : t) {
        mp1[c]++;
    }
    // mp1 now has the counts of each letter in string t.
    mp2 = mp1;
    // mp2 is an exact copy of mp1 now
    int l=0, r=0;
    while (r < (int)s.length()) {
        curr += s[r];
        if (mp2.count(s[r]) == 1) {
            // if the letter is present then reduce it's count by 1 in the map
            mp2[s[r]]--;
            if (mp2[s[r]] == 0) {
                // if the count of the letter has gone to zero then remove the key
                mp2.erase(s[r]);

                if (mp2.empty()) {
                    // if the map is empty now then check if the new substring is shorter than the result
                    if (curr.length() < result.length() || result=="") {
                        result = curr;
                    }
                    mp2 = mp1;
                    l++;
                    r = l;
                    curr = "";
                    continue;
                }
           }
        }
        r++;
    }
    return result;
}


int main() {
    string s, t;
    getline(cin, s);
    getline(cin, t);
    cout << minWindow(s, t) << endl;
}

/*input
a
aa
*/