#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>


using namespace std;

class Solution {
public:
    bool Find(int target, vector<vector<int> > array) {
        int m = array.size();
        int n = array[0].size();
        int r = 0, c = n - 1;
        if (array.empty() || m * n == 0) {
            return false;
        }
        while (r < m && c >= 0) {
            if (array[r][c] == target) {
                return true;
            } else if (array[r][c] > target) {
                c--;
            } else {
                r++;
            }
        }
        return false;
    }
};

int main() {
    Solution s;
    int a[4][4] = {{1, 2, 8,  9},
                   {2, 4, 9,  12},
                   {4, 7, 10, 13},
                   {6, 8, 11, 15}};
    vector<vector<int> > array(4, vector<int>(4));
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            array[i][j] = a[i][j];
        }
    }
    cout << s.Find(5, array) << endl;
    cout << s.Find(9, array) << endl;
    return 0;
}