# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot is None or k <= 0:
            return None
        res = list()

        def travel(root):
            if len(res) >= k or root is None:
                return
            travel(root.left)
            res.append(root)
            travel(root.right)

        travel(pRoot)
        if len(res) < k:
            return None
        return res[k - 1]
