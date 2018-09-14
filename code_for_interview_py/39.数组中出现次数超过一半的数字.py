# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        # 直接用字典存储出现次数
        d=dict()
        for i in numbers:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
            if d[i]*2>len(numbers):
                return i
        return 0