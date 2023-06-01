#include <vector>
#include <iostream>
#include <string>
using namespace std;

void print_board(vector<vector<char>> board) {
    for(auto i : board) {
        for(auto j : i) {
            cout << j << " ";
        }
        cout << endl;
    }
}

bool is_valid_sudoku(vector<vector<char>> board) {
    // we will create three 2D arrays to check for check for each of the three parameters
    bool check_row[9][9] = {false};
    bool check_box[9][9] = {false};
    bool check_col[9][9] = {false};
    for(int i=0; i<(int)board.size(); i++) {
        for(int j=0; j<(int)board.size(); j++) {
            if (board[i][j] != '.') {
                int num = stoi(string(1, board[i][j])) - 1;
                int box_num = j/3 + 3 *(i/3);
                if (check_row[i][num] || check_col[j][num] || check_box[box_num][num]) {
                    return false;
                } else {
                    check_row[i][num] = check_col[j][num] = check_box[box_num][num] = true;
                }
            }
        }
    }
    return true;
}

int main() {
    int n;
    cin >> n;
    vector<vector<char>> board(n, vector<char>(n));
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            char x;
            cin >> x;
            board[i][j] = x;
        }
    }
    // print_board(board);
    if(is_valid_sudoku(board)) {
        cout << "valid";
    } else {
        cout << "INVALID";
    }
    cout << endl;
    return 0;
}

/*input
9
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
*/

/*output
valid
*/