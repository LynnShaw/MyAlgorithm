# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, node):
        # write code here
        self.stackA.append(node)

    def pop(self):
        # return xx
        if len(self.stackB) == 0:
            while len(self.stackA) != 0:
                self.stackB.append(self.stackA.pop())
        if len(self.stackB) == 0:
            return None
        return self.stackB.pop()
