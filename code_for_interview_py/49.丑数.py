# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        res = [1]
        t2 = t3 = t5 = 0

        nextIdx = 1
        while nextIdx < index:
            minNum = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
            res.append(minNum)
            # [1,2,3,4,5,6,8,9,10,12,15,16,18,20,24]
            # 比如当前最小是24，则t2 t3均加一，t2上一位对应20->10->8 t3上一位对应18->6->5
            # 下一次对应30->15->10 27->9->7
            # 这三个if有可能进入一个或者多个，进入多个是三个队列头最小的数有多个的情况
            if res[t2] * 2 == minNum:
                t2 += 1
            if res[t3] * 3 == minNum:
                t3 += 1
            if res[t5] * 5 == minNum:
                t5 += 1

            nextIdx += 1

        return res[nextIdx - 1]
