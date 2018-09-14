# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if s == None or len(s) == 0:
            return 0
        d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        t = 0
        f = 1
        if s[0] == '+':
            t = 1
        if s[0] == '-':
            t = 1
            f = -1
        res = 0
        for i in s[t:]:
            if i in d:
                res = d[i] + res * 10
            else:
                return 0
        return res * f