# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        node = [root]
        res = []
        while len(node) != 0:
            t = node.pop(0)
            res.append(t.val)
            if t.left is not None:
                node.append(t.left)
            if t.right is not None:
                node.append(t.right)
        return res

