# -*- coding:utf-8 -*-
class Solution:
    def mycmp(self, x, y):
        x, y = str(x), str(y)
        if x + y > y + x:
            return 1
        elif x + y < y + x:
            return -1
        else:
            return 0

    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) == 0:
            return ""
        if len(numbers) == 1:
            return numbers[0]
        numbers.sort(cmp=self.mycmp)
        # print(numbers)
        return ''.join(str(x) for x in numbers)
