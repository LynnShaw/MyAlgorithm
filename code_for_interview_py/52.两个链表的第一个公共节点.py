# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        l1 = 0
        l2 = 0
        t1 = pHead1
        t2 = pHead2
        while pHead1 is not None:
            pHead1 = pHead1.next
            l1 += 1
        while pHead2 is not None:
            pHead2 = pHead2.next
            l2 += 1
        diff = abs(l1 - l2)
        if l1 > l2:
            while diff != 0:
                t1 = t1.next
                diff -= 1
        else:
            while diff != 0:
                diff -= 1
                t2 = t2.next
        while t1 != t2:
            t1 = t1.next
            t2 = t2.next
        return t1