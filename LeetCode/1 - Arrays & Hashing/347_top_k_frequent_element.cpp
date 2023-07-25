#include<bits/stdc++.h>
using namespace std;

class compare {
public:
    bool operator()(pair<int, int> lhs, pair<int, int> rhs) {
        return lhs.second < rhs.second;
    }
};

vector<int> top_k_frequent_elements(vector<int> input, int k) {
    unordered_map<int, int> mappy;
    for(int i : input) {
        mappy[i] = mappy[i] + 1;
    }
    priority_queue<pair<int, int>, vector<pair<int,int>>, compare> heap;
    for (auto it=mappy.begin(); it!=mappy.end(); it++) {
        heap.push(*it);
    }
    vector<int> output;
    for(int i=0; i<k; i++) {
        int x = heap.top().first;
        heap.pop();
        output.push_back(x);
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
1
1
1
*/