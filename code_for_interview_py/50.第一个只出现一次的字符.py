# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.d = dict()
        self.l = list()

    def FirstAppearingOnce(self):
        # write code here
        for i in self.l:
            if self.d[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        # write code here
        if char not in self.d:
            self.d[char] = 1
            self.l.append(char)
        else:
            self.d[char] += 1