#include <iostream>
#include <stack>
#include <vector>

using namespace std;


class Solution {
    stack<int> s1,s2;
public:
    void push(int value) {
        s1.push(value);
        if (s2.empty()||s1.top()<s2.top()) {
            s2.push(value);
        }
    }
    void pop() {
        if(s2.top() == s1.top()){
            s2.pop();
        }
        s1.pop();
    }
    int top() {
        return s1.top();
    }
    int min() {
        return s2.top();
    }
};

int main() {
    Solution s;
    s.push(6);
    s.push(4);
    s.push(2);
    s.push(5);
    s.push(3);
    cout<<s.min()<<endl;
    s.push(1);
    cout<<s.min()<<endl;
    cout<<s.top()<<endl;
    s.pop();
    cout<<s.min()<<endl;

    return 0;
}