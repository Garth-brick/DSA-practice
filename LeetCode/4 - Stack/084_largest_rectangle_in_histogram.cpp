#include <iostream>
#include <vector>
#include <stack>
#include <utility>
#include <algorithm>
using namespace std;

// ----------------------------------------
// very good attempt but exceeds time limit
// ----------------------------------------


// IMPORTANT LOGIC: Every maximal rectangle must contain atleast one full bar

// while going through all bars from left to right our objective is to figure out how far we can extend each bar to create a recatangle from that bar
// Once we can see the rectangles created by each bar we can easily pich the biggest one
// case-1: if we get a bar that is smaller than the stacked bar --> the stacked bar can no longer be extended and should be popped from the stack, it's maximal rectnagle has been found now.
// case-2 if we get a bar that is greater or equal to the stacked bar --> the stacked bar can still be extended further


int largestRectangleArea(vector<int>& heights) {
    stack<pair<int, int>> stacky;
    // this will be storing {index, height}

    int max_area = 0;
    int _h;

    for (int i=0; i<(int)heights.size(); i++) {
        // go over each of the bars in order from left to right
        _h = heights[i];

        while (!stacky.empty() && _h < stacky.top().second) {
            // if we get a bar that is lower than one in the stack then we can't extend a rectangle from that bar in the stack
            // so we pop that bar  from the stack and take its rectangle if its greater than the max_area we already had
            max_area = max(max_area, stacky.top().second*(i-stacky.top().first));
            stacky.pop();
        }

        // if we get a bar that is higher or at the same height as the bars in the stack then we can just push this bar onto the stack as usual and continue extending all the bars
        // while pushing a bar we also need to see how far we could've extended it to the left
        int l=i;
        while (l >= 0) {
            if (heights[l] < _h) {
                break;
            }
            l--;
        }
        stacky.push({l+1, _h});
        // doing l+1 because it got decremented one extra time before the loop was broken
    }

    while (!stacky.empty()) {
        max_area = max(max_area, stacky.top().second*(int)(heights.size()-stacky.top().first));
        stacky.pop();
    }

    return max_area;
}


int main() {
    vector<int> input_heights = {2,1,5,6,2,3};
    cout << largestRectangleArea(input_heights) <<endl;
}