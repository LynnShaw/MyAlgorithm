# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        return [i for i in array if i % 2 != 0] + [i for i in array if i % 2 == 0]
