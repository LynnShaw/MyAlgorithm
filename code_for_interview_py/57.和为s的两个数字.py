# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if array is None or len(array) == 0:
            return []
        a, b = 0, len(array) - 1
        while a != b:
            if array[a] + array[b] == tsum:
                return (array[a], array[b])
            elif array[a] + array[b] > tsum:
                b -= 1
            else:
                a += 1
        return []
