# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        n = len(numbers)
        for i in range(n):
            if numbers[numbers[i] % n] >= n:
                duplication[0] = numbers[i] % n
                return True
            numbers[numbers[i] % n] += n
        return False
