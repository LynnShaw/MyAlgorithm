#include <iostream>
#include <stack>
#include <vector>

using namespace std;


class Solution
{
public:
    void push(int node) {
        stack1.push(node);
    }

    int pop() {
        if (stack1.empty()){
            return -1;
        }
        while (!stack1.empty()){
            stack2.push(stack1.top());
            stack1.pop();
        }
        int result = stack2.top();
        stack2.pop();
        while (!stack2.empty()){
            stack1.push(stack2.top());
            stack2.pop();
        }
        return result;
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};


int main() {
    Solution s;
    s.push(1);
    s.push(2);
    s.push(3);
    s.push(5);
    cout<<s.pop()<<endl;
    cout<<s.pop()<<endl;
    cout<<s.pop()<<endl;
    cout<<s.pop()<<endl;
    cout<<s.pop()<<endl;
    return 0;
}