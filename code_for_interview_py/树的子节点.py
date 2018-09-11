# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 is None or pRoot2 is None:
            return False
        if pRoot1.val == pRoot2.val:
            result = self.contain(pRoot1, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def contain(self, root1, root2):
        if root1 is None and root2 is not None:
            return False
        if root2 is None:
            return True
        if root1.val != root2.val:
            return False
        return self.contain(root1.left, root2.left) and self.contain(root1.right, root2.right)
