#include <iostream>
#include <stack>
#include <vector>

using namespace std;


struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};
class Solution {
public:
    int TreeDepth(TreeNode* pRoot)
    {
        if (pRoot == NULL){
            return 0;
        }
//        int l = TreeDepth(pRoot->left);
//        int r = TreeDepth(pRoot->right);
//
//        return l>r?(l+1):(r+1);
        if (pRoot->right == NULL && pRoot->left==NULL){
            return 1;
        } else if (pRoot->left !=NULL && pRoot->right==NULL){
            return 1+TreeDepth(pRoot->left);
        } else if (pRoot->left==NULL && pRoot->right!=NULL){
            return 1+TreeDepth(pRoot->right);
        } else{
            return max(TreeDepth(pRoot->right),TreeDepth(pRoot->left))+1;
        }
    }
};
int main() {
    Solution s;


    return 0;
}