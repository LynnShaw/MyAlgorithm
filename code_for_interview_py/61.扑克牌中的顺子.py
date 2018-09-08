# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) != 5:
            return False
        numbers.sort()
        zero_cnt = numbers.count(0)
        if max(numbers) - min(numbers[zero_cnt:]) >= 5 or len(set(numbers[zero_cnt:])) != 5 - zero_cnt:
            return False
        return True