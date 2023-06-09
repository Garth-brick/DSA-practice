#include <iostream>
#include <deque>
#include <vector>
using namespace std;

void print_vector(vector<int> vect) {
    for (int i : vect) {
        cout << i << " ";
    }
    cout << endl;
}

    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> q;
        vector<int> result;
        int l=0, r=0;
        while (r < (int)nums.size()) {
            int _r = nums[r];
            int _l = nums[l];

            // Put nums[r] into q at the right place
            // if the current number is the greatest then the entire queue should get cleared because those numbers will never be needed now and the incoming number should be placed at the head.
            while (!q.empty()) {
                if (q.back() < _r) {
                    q.pop_back();
                } else {
                    break;
                }
            }
            q.push_back(_r);
            

            r++;
            if (r-l+1 > k) {
                result.push_back(q.front());
                if (q.front() == _l) {
                    q.pop_front();
                }
                l++;
            }
        }
        return result;
    }


int main() {
    int k, _size;
    cin >> k >> _size;
    vector<int> vect(_size);
    for (int i=0; i<_size; i++) {
        cin >> vect[i];
    }
    print_vector(maxSlidingWindow(vect, k));
}

/*input
3
8
1 3 -1 -3 5 3 6 7
*/