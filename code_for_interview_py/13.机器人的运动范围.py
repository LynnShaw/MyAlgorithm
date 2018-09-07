# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        self.s = set()
        self.row = rows
        self.col = cols
        self.dfs(threshold, 0, 0)
        return len(self.s)

    def judge(self, threshold, i, j):
        return sum(map(int, list(str(i))))+sum(map(int, list(str(j)))) <= threshold

    def dfs(self, threshold, r, c):
        if not self.judge(threshold, r, c) or (r, c) in self.s:
            return
        self.s.add((r, c))
        if r+1 < self.row:
            self.dfs(threshold, r+1, c)
        if c+1 < self.col:
            self.dfs(threshold, r, c+1)
