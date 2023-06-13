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
    stack<pair<int,int>> stacky;
    // this will keep the temperatrue and the index of the specific
    int _t;
    int i = 0;
    while (i < (int)temperatures.size()) {
        _t = temperatures[i];

        if (stacky.empty() || _t <= stacky.top().first) {
            stacky.push({_t,i});
            i++;
            continue;
        }

        while (!stacky.empty() && _t > stacky.top().first) {
            result[stacky.top().second] = i - stacky.top().second;
            stacky.pop();
        }
    }
    return result;
}


int main() {
    vector<int> vect = {89,62,70,58,47,47,46,76,100,70};
    print_vector(dailyTemperatures(vect));
}