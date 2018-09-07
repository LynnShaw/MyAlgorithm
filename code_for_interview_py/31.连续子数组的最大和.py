# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        res = -999999  # 避免全为负数的情况
        cur = 0
        for i in array:
            cur += i
            res = max((res,cur))
            if cur < 0:
                cur = 0
        return res