#include <iostream>
#include <stack>
#include <vector>
#include <string>
using namespace std;


bool isValid(string s) {
    stack<char> stacky;

    for (char c : s) {
        if (c=='(' || c=='{' || c=='[') {
            stacky.push(c);
            continue;
        }
        else if (stacky.empty()) {
            return false;
        }

        if (stacky.top()=='(' && c==')') {
            stacky.pop();
        }
        else if (stacky.top()=='{' && c=='}') {
            stacky.pop();
        }
        else if (stacky.top()=='[' && c==']') {
            stacky.pop();
        }
        else {
            return false;
        }
    }

    if (stacky.empty()) return true;
    return false;
}


int main() {
    string s;
    getline(cin, s);
    cout << isValid(s);
}

/*input
(]
*/