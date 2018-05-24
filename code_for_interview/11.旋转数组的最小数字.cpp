#include <iostream>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    int minNumberInRotateArray(vector<int> rotateArray) {

        int length = rotateArray.size();
        if (length == 0) {
            return 0;
        }

        int left = 0, right = length - 1;
        int mid = (left + right) / 2;

        while (rotateArray[left] >= rotateArray[right]) {
            if (left == right - 1) {
                return rotateArray[right];
            }

            mid = (left + right) / 2;
            if (rotateArray[left] == rotateArray[mid] && rotateArray[left] == rotateArray[right]) {
                int min = rotateArray[0];
                for (int i = 0; i < length; ++i) {
                    if (min > rotateArray[i]) {
                        return rotateArray[i];
                    }
                    min = rotateArray[i];
                }
            }
            if (rotateArray[left] <= rotateArray[mid]) {
                left = mid;
            //} else if (rotateArray[right] >= rotateArray[mid]) {
            } else {
                right = mid;
            }
        }
        return rotateArray[mid];
    }
};


int main() {
    Solution s;
//    int a[] = {3, 4, 5, 6, 7, 1, 2};
//    int a[] = {1, 1, 1, 1, 1, 0, 1};
    int a[]={6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335};
    vector<int> v(a, a +30);
    cout << s.minNumberInRotateArray(v);
    return 0;
}