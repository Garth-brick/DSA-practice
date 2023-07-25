#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cmath>
using namespace std;


void print_vector(vector<string> vect) {
    for (string s : vect) {
        cout << s << endl;
    }
}


vector<string> result;

    void backtrack(int open_count, int closed_count, string current, int n) {
        if (closed_count == n) {
            result.push_back(current);
            return;
        }

        if (open_count < n) {
            backtrack(open_count+1, closed_count, current+"(", n);
        }
        if (closed_count < open_count) {
            backtrack(open_count, closed_count+1, current+")", n);
        }
    }


vector<string> generateParenthesis(int n) {
    // only add an open bracket if open_count < n
    // only add a closed bracket if closed < open
    // keep adding until open_count == closed_count == n
    backtrack(0, 0, "", n);
    return result;
}


int main() {
    int n;
    cin >> n;
    print_vector(generateParenthesis(n));
}


/*input
3
*/