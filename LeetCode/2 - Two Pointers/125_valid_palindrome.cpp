#include <iostream>
#include <string>
using namespace std;

bool is_valid_palindrome(string s) {
    for(int i=0; i<(int)s.size(); i++) {
        if (s[i]>=65 && s[i]<=90) {
            s[i] += 32;
        }
    }
    int i=0, j=s.size()-1;
    while(i<j) {
        if((s[i]<97 && s[i]>57) || s[i]>122 || s[i]<48) {
            i++; 
            continue;
        }
        if((s[j]<97 && s[j]>57) || s[j]>122 || s[j]<48) {
            j--; 
            continue;
        }
        if (s[i] != s[j]) {
            cout << "(" << i << "," << j << ")" << endl;
            return false;
        }
        cout << "(" << i << "," << j << ")" << endl;
        i++;
        j--;
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
0P
*/