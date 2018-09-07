# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pret = ListNode(0)
        #pHead.next = None
        pHead = pret
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                pHead.next = pHead2
                pHead2 = pHead2.next
            else:
                pHead.next = pHead1
                pHead1 = pHead1.next
            pHead=pHead.next

        if pHead1 is None:
            pHead.next = pHead2
        elif pHead2 is None:
            pHead.next = pHead1
        return pret.next
