#include <iostream>
#include <vector>
#include <map>
using namespace std;


// works but slow


int carFleet(int target, vector<int>& position, vector<int>& speed) {
    map<int, double> eta;
    for (int i=0; i<(int)position.size(); i++) {
        // soring the ETA of each car with its position in a map
        // the question says that the starting position of each car is unique

        eta[-position[i]] = (double)(target-position[i])/speed[i];
        // storinng position with a negative sign because we want to sort in descending order and the default sorting in a map is in ascending order
    }

    int num_fleets = 0;
    // this will get incremented whenever we find a car that's slower than the cars ahead of it 
    // IMPORTANT LOGIC: if X starts from behind Y and Y has a larger ETA then they will be in the same fleet

    double curr_slowest = 0; // this will track the slowest car --> this becomes the leader of each fleet
    
    for (pair<int, double> p : eta) {
        // travesing the cars from the car that's furtherst up ahead to the car that's last in the line
        // no car can overtake so this order will always be maintained

        if (p.second > curr_slowest) {
            // if a car is slower than the 
            curr_slowest = p.second;
            num_fleets++;
        }
    }
    return num_fleets;
}


int main() {
    vector<int> input_position = {10,8,0,5,3};
    vector<int> input_speed = {2,4,1,1,3};
    int input_target = 12;
    cout << carFleet(input_target, input_position, input_speed) << endl;
}