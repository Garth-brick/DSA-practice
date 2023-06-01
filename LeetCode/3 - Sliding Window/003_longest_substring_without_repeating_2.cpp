#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

int longest_non_repeating_substring(string s) {
    unordered_set<char> char_set;
    int l=0, r=0, result=0;
    while(r < (int)s.size()) {
        while(char_set.count(s[r]) == 1) {
            char_set.erase(s[l]);
            l++;
        }
        char_set.insert(s[r]);
        result = max(result, r-l+1);
        r++;
    }
    return result;
}

int main() {
    string input;
    getline(cin, input);
    cout << longest_non_repeating_substring(input);
}

/*input
dvdf
*/