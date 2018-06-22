# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        m = len(array)
        n = len(array[0])
        i, j = 0, n-1
        while i < m and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
