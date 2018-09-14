# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        small = 1
        large = 2
        middle = (tsum + 1) / 2
        cursum = small + large
        out = []
        while small < middle:
            if cursum == tsum:
                out.append(list(range(small, large + 1)))
            while cursum > tsum and small < middle:
                cursum -= small
                small += 1
                if cursum == tsum:
                    out.append(list(range(small, large + 1)))
            large += 1
            cursum += large
        return out