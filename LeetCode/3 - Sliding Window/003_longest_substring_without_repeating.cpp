#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

int longest_non_repeating_substring(string s) {
    if (s.size()==0) return 0;
    
    int l=0, r=1, result=0;
    unordered_set<char> unique;
    unique.insert(s[l]);
    while(r < (int)s.size()) {
        if (unique.count(s[r]) == 1) {
            result = max(result, r-l);
            unique.clear();
            l++;
            r = l+1;
            unique.insert(s[l]);
        } else {
            unique.insert(s[r]);
            r++;
        }
    }
    result = max(result, r-l);
    return result;
}

int main() {
    string input;
    getline(cin, input);
    cout << longest_non_repeating_substring(input);
}

/*input
au
*/