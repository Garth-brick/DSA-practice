#include <iostream>
#include <vector>
using namespace std;


bool searchMatrix(vector<vector<int>>& matrix, int target) {
    // i'm just gonna act as if the matrix was just one long sorted array
    int l=0, r=(int) (matrix.size()*matrix[0].size())-1;

    while (l<=r) {
        int mid = (r+l)/2;
        int col = mid % matrix[0].size();
        int row = mid / matrix[0].size();

        if (matrix[row][col] < target) {
            l = mid + 1;
        } else if (matrix[row][col] > target) {
            r = mid - 1;
        } else {
            return true;
        }
    }
    return false;
}


int main() {
    vector<vector<int>> input_matrix = {{1,3,5,},{10,11,16,2},{23,30,34,6}};
    int target = 4;
    cout << searchMatrix(input_matrix, target);
}