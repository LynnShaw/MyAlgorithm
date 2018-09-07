# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        root.right,root.left=root.left,root.right
        if root.right is not None:
            self.Mirror(root.right)
        if root.left is not None:
            self.Mirror(root.left)