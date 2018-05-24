#include <iostream>
#include <stack>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    struct ListNode *next;

    ListNode(int x) :
            val(x), next(NULL) {}
};

class Solution {
public:
    vector<int> printListFromTailToHead(ListNode *head) {
        vector<int> v;
        stack<int> s;

        while (head!=NULL){
            s.push(head->val);
            head=head->next;
        }
        while (!s.empty()){
            v.push_back(s.top());
            s.pop();
        }
        return v;
    }
};

int main() {
    ListNode l1(1);
    ListNode l2(2);
    ListNode l3(3);
    ListNode l4(4);
    l1.next=&l2;
    l2.next=&l3;
    l3.next=&l4;

    ListNode *L=&l1;
    while(L){
        cout<<L->val<<" ";
        L=L->next;
    }
    cout<<endl;
    Solution s;
    vector<int> v=s.printListFromTailToHead(&l1);
    for (int i = 0; i <v.size(); ++i) {
        cout<<v[i]<<" ";
    }
    return 0;
}