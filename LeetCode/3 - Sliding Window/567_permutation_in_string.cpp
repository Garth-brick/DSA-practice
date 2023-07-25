#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;


void print_array(int * arr) {
    for (int i=0; i<26; i++) {
        cout << (char)(i+97) << " ";
    }
    cout << endl;
    for (int i=0; i<26; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}


bool all_zero(int * arr) {
    for (int i=0; i<26; i++) {
        if (arr[i] != 0) {
            return false;
        }
    }
    return true;
}


bool checkInclusion(string s1, string s2) {
    int arr1[26] = {0};
    for (char c : s1) {
        arr1[c - 97]++;
    }
    int arr2[26];
    copy(arr1, arr1+26, arr2);
    print_array(arr1);
    cout << "START" << endl;
    int l=0, r=0;
    while (r < (int) s2.size()) {
        
        if (arr2[s2[r]-97] == 0) {
            l++;
            r = l;
            copy(arr1, arr1+26, arr2);
            cout << "------- RESET ------- l = " << l << endl;
            continue;
        }
        else {
            arr2[s2[r]-97]--;
            print_array(arr2);
            if (all_zero(arr2)) {
                return true;
            }
        }
        r++;
    }
    return false;
}


int main() {
    string str1, str2;
    getline(cin, str1);
    getline(cin, str2);
    cout << checkInclusion(str1, str2);
}
/*input
adc
dcda
*/