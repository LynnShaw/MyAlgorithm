#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

class Solution {
public:
    // Parameters:
    //        numbers:     an array of integers
    //        length:      the length of array numbers
    //        duplication: (Output) the duplicated number in the array number
    // Return value:       true if the input is valid, and there are some duplications in the array number
    //                     otherwise false
    bool duplicate(int numbers[], int length, int *duplication) {
//        int a[length+1]={0};
        int *a = new int[length];
        memset(a, 0, sizeof(int) * length);
        for (int i = 0; i < length; ++i) {
            if (a[numbers[i]] == 1) {
                for (int j = 0; j < length; ++j) {
                    cout<<a[j];
                }
                *duplication = numbers[i];
                cout << *duplication << endl;
                return true;
            } else {
                a[numbers[i]]++;
            }
        }
        return false;

    }
};

int main() {
    int num[] = {2, 1, 3, 1, 4};
    int *dup=0;
    Solution s;
    int duplication;
    bool b = s.duplicate(num, 5, &duplication);
    cout << b << endl;
    return 0;
}