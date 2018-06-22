# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right is not None:
            pNode=pNode.right
            while pNode.left is not None:
                pNode=pNode.left
            return pNode
        else:
            while pNode.next is not None:
                parent = pNode.next
                if parent.left==pNode:
                    return parent
                pNode=pNode.next
        return None