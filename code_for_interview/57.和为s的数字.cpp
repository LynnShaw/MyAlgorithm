#include <iostream>
#include <stack>
#include <vector>

using namespace std;


class Solution {
public:
    vector<int> FindNumbersWithSum(vector<int> array, int sum) {
        vector<int> v;
        if (array.size() < 2) {
            return v;
        }
        int i = 0, j = array.size() - 1;
        while (i != j) {
            int cur = array[i] + array[j];
            if (cur == sum) {
                v.push_back(array[i]);
                v.push_back(array[j]);
                return v;
            } else if (cur>sum){
                j--;
            } else{
                i++;
            }
        }
        return v;
    }
};

int main() {
    Solution s;
    int a[] = {1,2,4,7,11,15};
    vector<int> v(a,a+6);
    vector<int> r = s.FindNumbersWithSum(v,15);
    cout<<r[0]<<r[1]<<endl;
    return 0;
}