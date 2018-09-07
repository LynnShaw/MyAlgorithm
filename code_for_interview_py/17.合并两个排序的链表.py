# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        pMerge = None
        if pHead1.val<pHead2.val:
            pMerge=pHead1
            pMerge.next = self.Merge(pHead1.next,pHead2)
        else:
            pMerge=pHead2
            pMerge.next = self.Merge(pHead1,pHead2.next)
        
        return pMerge