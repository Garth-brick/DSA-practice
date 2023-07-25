#include <iostream>
#include <string>
using namespace std;

bool is_valid_palindrome(string s) {
    int l=0, r=s.size()-1;
    while(l<r) {
        if (!isalnum(s[l])) { // built-in function for checking if a character is alphanumeric
            l++;
        }
        else if (!isalnum(s[r])) {
            r--;
        }
        // use the built-in function to convert to lower-case if needed
        else if (tolower(s[l]) != tolower(s[r])) {
            return false;
        }
        else {
            l++;
            r--;
        }
    }
    return true;
}

int main() {
    string input;
    getline(cin, input);

    if(is_valid_palindrome(input)) {
        cout << "valid";
    } else {
        cout << "INVALID";
    }
    cout << endl;
    return 0;
}

/*input
pop
*/