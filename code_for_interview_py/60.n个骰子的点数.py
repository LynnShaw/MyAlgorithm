# -*- coding:utf-8 -*-
class Solution:
    def PrintProbability(self, number):
        # write code here
        if number < 1:
            return
        maxvalue = 6
        dp = [[0 for i in range(maxvalue * number)] for i in range(number)]
        for i in range(maxvalue):
            dp[0][i] = 1

        for i in range(1, number):  # 1代表两个，所以下面+1
            for j in range(i, 6 * (i + 1)):  # i之前的概率为0
                # print(j)
                dp[i][j] = dp[i - 1][j - 6] + dp[i - 1][j - 5] + dp[i - 1][j - 4] + \
                           dp[i - 1][j - 3] + dp[i - 1][j - 2] + dp[i - 1][j - 1]

        # print(dp)
        cnt = [i / sum(dp[number - 1]) for i in dp[number - 1]]
        return cnt