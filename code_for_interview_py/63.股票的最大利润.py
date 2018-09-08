# -*- coding:utf-8 -*-
class Solution:
    def Max_Diff_Solution(self, n):
        # write code here
        if n is None or len(n) == 0:
            return 0
        min_num = n[0]
        max_diff = n[1] - min_num
        for i in n[2:]:
            if i < min_num:
                min_num = i
            cur_diff = i - min_num
            if cur_diff > max_diff:
                max_diff = cur_diff
        return max_diff