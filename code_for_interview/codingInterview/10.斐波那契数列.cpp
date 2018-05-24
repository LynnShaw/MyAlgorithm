#include <iostream>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    int Fibonacci(int n) {
        // int a,b,c;
        int a = 0,b = 0,c = 0;
        for (int i = 1; i <= n; ++i) {
            if (i==1){
                c=1;
            } else if(i==2){
                b=0;
                a=1;
                c=1;
            } else {
                b = a;
                a = c;
                c = b + a;
            }
        }
        return c;
    }
};
int main() {
    Solution s;
    cout<<s.Fibonacci(1)<<endl;
    cout<<s.Fibonacci(2)<<endl;
    cout<<s.Fibonacci(3)<<endl;
    cout<<s.Fibonacci(5)<<endl;
    cout<<s.Fibonacci(7)<<endl;
    return 0;
}