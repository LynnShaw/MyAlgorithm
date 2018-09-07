# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n < 0:
            n += 2**32
        cnt = 0
        while(n != 0):
            cnt += 1
            n &= (n-1)
#             print(n)
        return cnt
