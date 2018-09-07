# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        isneg = 1
        if exponent < 0:
            exponent = -exponent
            isneg = 0
        result = self.Power(base*base, exponent//2)
        if exponent % 2 != 0:
            result *= base
        return (result if isneg == 1 else 1/result)
#return base**exponent
