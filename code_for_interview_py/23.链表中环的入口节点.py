# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        pA, pB = pHead, pHead
        while pB and pB.next:
            pA = pA.next
            pB = pB.next.next
            if pA == pB:
                pC = pHead
                while pC != pA:
                    pA = pA.next
                    pC = pC.next
                return pC
        return None