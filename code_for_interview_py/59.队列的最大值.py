# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if num is None or size <= 0:
            return []
        deq = []
        # 保存最大值，以及最大值后面出现的数（可能成为最大值，只保存后面出现的最大的），判断最大值是否过期
        if len(num) >= size:
            index = []
            # 第一个窗口
            for i in range(size):
                # index = 0 的数最大
                while len(index) > 0 and num[i] > num[index[-1]]:
                    index.pop()
                index.append(i)
            # print(index)

            for i in range(size, len(num)):
                deq.append(num[index[0]])
                # 移除比当前数字小的数
                while len(index) > 0 and num[i] > num[index[-1]]:
                    index.pop()
                # 移除不在窗口里的最大数
                if len(index) > 0 and index[0] <= i - size:
                    index.pop(0)
                index.append(i)
                # print(index)

            deq.append(num[index[0]])
        return deq
