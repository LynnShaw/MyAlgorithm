# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if root.left is None and root.right is None:
            if root.val == expectNumber:
                return [[root.val]]
            else:
                return []
        a = self.FindPath(root.left, expectNumber - root.val) + self.FindPath(root.right, expectNumber - root.val)
        return [[root.val] + i for i in a]
