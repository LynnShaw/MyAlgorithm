# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        pre1 = 0
        pre2 = 1
        for _ in range(1, number+1):
            cur = pre1+pre2
            pre1 = pre2
            pre2 = cur
        return cur
