#include <iostream>
#include <vector>
#include <stack>
#include <utility>
#include <algorithm>
using namespace std;


// works but slow


int carFleet(int target, vector<int>& position, vector<int>& speed) {
    vector<pair<int,int>> pos_speed(position.size());
    for(int i=0; i<(int)position.size(); i++) {
        pos_speed[i] = {position[i], speed[i]};
    }

    stack<float> eta;
    // this will end up string the ETAs of each fleet

    sort(pos_speed.begin(), pos_speed.end());

    for (int i=0; i<(int)pos_speed.size(); i++) {
        // we will go over each car in acending order of position, last car to the first car

        float time = (float)(target-pos_speed[i].first)/pos_speed[i].second;

        while (!eta.empty() && eta.top() <= time) {
            // if the ETA of a car that was behind was less than the ETA of a car that was ahead of it then the ETA of the car that was behind will get popped and replaced by the ETA of the car in front
            eta.pop();
        }

        eta.push(time);
        // we push the ETA of the car in every case
    }
    return (int)eta.size();
}


int main() {
    vector<int> input_position = {10,8,0,5,3};
    vector<int> input_speed = {2,4,1,1,3};
    int input_target = 12;
    cout << carFleet(input_target, input_position, input_speed) << endl;
}