#include<bits/stdc++.h>
using namespace std;

vector<int> top_k_frequent_elements(vector<int> nums, int k) {
    unordered_map<int, int> mappy;
    for(int i : nums) {
        mappy[i]++;
    }
    priority_queue<pair<int, int>> heap;
    for (auto i : mappy) {
        // putting the count as the first element in the pair because it will be used for the default sorting in the heap
        heap.push(make_pair(i.second, i.first));
    }
    vector<int> output;
    for(int i=0; i<k; i++) {
        output.push_back(heap.top().second);
        heap.pop();
    }
    return output;
}

void print_vector(vector<int> vect) {
    for (int i : vect) {
        cout << i << " ";
    }
    cout << endl;
}

int main() {
    int k;
    cin >> k;
    int n;
    cin >>  n;
    vector<int> input;
    for (int i=0; i<n; i++) {
        int x;
        cin >> x;
        input.push_back(x);
    }

    vector<int> output = top_k_frequent_elements(input, k);
    print_vector(output);
}

/*input
2
6
1 1 1 2 2 3
*/