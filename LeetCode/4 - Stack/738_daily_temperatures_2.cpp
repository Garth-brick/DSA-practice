#include <vector>
#include <stack>
#include <iostream>
#include <utility>
using namespace std;


// works but too slow


void print_vector(vector<int> vect) {
    for (int i : vect) {
        cout << i << " ";
    }
    cout << endl;
}



vector<int> dailyTemperatures(vector<int>& temperatures) {
    vector<int> result(temperatures.size());
    stack<int> stacky;
    // this will keep the index of the next greatest element to the right
    int _t;
    int i = (int)temperatures.size() - 1;

    // going from right to left
    while (i >= 0) {
        _t = temperatures[i];
        
        if (!stacky.empty() && _t < temperatures[stacky.top()]) {
            // if the top of the stack is less that the current temperature then the answer at that position has been found
            result[i] = stacky.top()-i;
        }

        if (!stacky.empty() && _t >= temperatures[stacky.top()]) {
            // if the current temperature is greater than the top of the stack then we can forget about the top of the stack because it will never be the next greatest element to anything now
            stacky.pop();
            continue;
        }
        stacky.push(i);
        i--;
    }
    return result;
}


int main() {
    //                  0  1  2  3  4  5  6  7  8   9
    vector<int> vect = {89,62,70,58,47,47,46,76,100,70};
    print_vector(dailyTemperatures(vect));
}