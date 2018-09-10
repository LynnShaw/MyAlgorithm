# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        cur = pHead
        pre = None
        next = None
        if pHead is None or pHead.next is None:
            return pHead
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre