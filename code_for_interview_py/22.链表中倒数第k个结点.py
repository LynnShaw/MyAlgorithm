# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        pA = head
        if head is None or k <= 0:
            return None
        for _ in range(k - 1):
            if pA.next is None:
                return None
            else:
                pA = pA.next
        pB = head
        while pA.next is not None:
            pA = pA.next
            pB = pB.next
        return pB