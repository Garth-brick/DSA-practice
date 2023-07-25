#include <iostream>
#include <stack>
#include <vector>
#include <string>
using namespace std;

template <typename T>
void print_vector(vector<T> v) {
    for (T t : v) {
        cout << to_string(t) << " ";
    }
    cout << endl;
}


vector<int> next_greater_element(vector<int> input) {
    stack<int> stacky;
    vector<int> result(input.size());
    for (int i=input.size()-1; i>=0; i--) {
        if (stacky.empty()) {
            result[i] = 0;
        }

        while (!stacky.empty() && input[i] >= stacky.top()) {
            stacky.pop();
        }
        result[i] = stacky.empty() ? 0 : stacky.top();

        stacky.push(input[i]);
    }
    return result;
}


int main() {
    vector<int> input_vector = {5,4,3,7,1};
    print_vector(next_greater_element(input_vector));
    return 0;
}