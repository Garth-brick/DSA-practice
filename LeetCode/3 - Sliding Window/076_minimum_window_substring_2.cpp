#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

// time O(n)
// storage O(n)

string minWindow(string s, string t) {

    if (t.empty() || s.empty()) return "";

    unordered_map<char, int> mp_t, mp_win;
    for (char c : t) mp_t[c]++;
    // mp_t is going to store frequency of each character in t
    // mp_win is going to store the frequency of each character in the window

    int valid_letter_count=0;
    // this will keep track of how many letters have we satisfied in the current window. If the valid_letter_count == mp_t.size()

    int l=0, r=0;
    int result_indices[2] = {0, INT_MAX};
    while (r < (int)s.length()) {

        if (mp_t.count(s[r]) > 0) {
            // if the letter is in mp_t then increment it in mp_win
            mp_win[s[r]]++;

            if (mp_win[s[r]] == mp_t[s[r]]) {
                // if there is enough of one letter then increment valid_letter_count
                valid_letter_count++;
            }
        }

        while (valid_letter_count == (int)mp_t.size()) {
            // if all the letters in mp_t are now in mp_win
            // then start shifting the left pointer

            while (mp_win.find(s[l]) == mp_win.end()) {
                // if the left pointer character is not in the window at all then just increment the left pointer
                l++;
            }
            while (mp_win.find(s[l])!=mp_win.end() && mp_win[s[l]] > mp_t[s[l]]) {
                // if the left pointer character is occurs more than needed then increment the left pointer and reflect this change by dropping it from the window
                mp_win[s[l]]--;
                l++;
            }

            if (r-l < result_indices[1]-result_indices[0]) {
                // if the new result is shorter than the previously stored result then update the result indices 
                result_indices[0] = l;
                result_indices[1] = r;
            }

            if (mp_win.find(s[l])!=mp_win.end() && mp_win[s[l]]==mp_t[s[l]]) {
                // if the left pointer is at a character which will make the window invalid if dropped then decrement the valid_letter_count, this will also break the loop and make the right pointer start moving forwards again
                valid_letter_count--;
                mp_win[s[l]]--;
                l++;
            }
        }
        r++;
    }
    return result_indices[1]-result_indices[0]==INT_MAX ? "" : s.substr(result_indices[0], result_indices[1]-result_indices[0]+1);
}


int main() {
    string s, t;
    getline(cin, s);
    getline(cin, t);
    cout << minWindow(s, t) << endl;
}

/*input
edeioridibadsjhedxc
ab
*/