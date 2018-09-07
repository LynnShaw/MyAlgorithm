# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):  # 旧链表的头
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        next = pHead.next
        pHead.next = None
        newHead = self.ReverseList(next)
        next.next = pHead
        return newHead   # 新链表的尾