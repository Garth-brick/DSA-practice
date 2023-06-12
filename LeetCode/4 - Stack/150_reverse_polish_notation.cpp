#include <iostream>
#include <stack>
#include <vector>
#include <string>
using namespace std;

int evalRPN(vector<string>& tokens) {
    stack<int> stacky;
    vector<string> ops = {"+", "-", "*", "/"};
    for (string s : tokens) {
        bool is_digit = true;
        for(int i=0; i<4; i++) {
            if (s==ops[i]) {
                is_digit = false;
                int param1 = stacky.top();
                stacky.pop();
                int param2 = stacky.top();
                stacky.pop();
                switch (i) {
                    case 0: stacky.push(param2 + param1); break;
                    case 2: stacky.push(param2 * param1); break;
                    case 1: stacky.push(param2 - param1); break;
                    case 3: stacky.push(param2 / param1); break;
                }
                break;
            }
        }

        if (is_digit) {
            stacky.push(stoi(s));
        }   
    }
    return stacky.top();
}


int main() {
    vector<string> dummy_input = {"10","6","9","3","+","-11","*","/","*","17","+","5","+"};
    cout << evalRPN(dummy_input) << endl;
}