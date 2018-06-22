# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        pre1 = 0
        pre2 = 1
        for _ in range(2, n+1):
            cur = pre1+pre2
            pre1 = pre2
            pre2 = cur
        return cur