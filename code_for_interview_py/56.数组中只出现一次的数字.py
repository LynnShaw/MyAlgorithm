# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if array is None or len(array) == 0:
            return []
        resOr = 0
        for i in array:
            resOr ^= i
        index1 = str(bin(resOr))[2:][::-1].find('1')

        num1 = 0
        num2 = 0
        for j in array:
            if str(bin(j))[2:][::-1].find('1') == index1:
                # print(j,str(bin(j))[2:-1])
                num1 ^= j
            else:
                num2 ^= j
        return (num1, num2)