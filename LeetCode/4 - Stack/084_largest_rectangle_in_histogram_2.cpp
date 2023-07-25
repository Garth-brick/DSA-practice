#include <iostream>
#include <vector>
#include <stack>
#include <utility>
#include <algorithm>
using namespace std;


// this solution works and is very smiilar to teh first one but I never really understood what's going on and how they came to discover this approach


int largestRectangleArea(vector<int>& heights) {
    stack<int> st;
    int ans=0;
    heights.push_back(0);
    for(int i=0; i<(int)heights.size(); i++) {
        while(!st.empty() && heights[st.top()]>heights[i]) {
            int top=heights[st.top()];
            st.pop();
            int ran=st.empty()?-1:st.top();
            ans=max(ans,top*(i-ran-1));
        }
        st.push(i);
    }
    return ans;
}


int main() {
    vector<int> input_heights = {10,10,9,10};
    cout << largestRectangleArea(input_heights) <<endl;
}