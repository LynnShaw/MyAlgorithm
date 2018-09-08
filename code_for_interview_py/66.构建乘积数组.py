# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        l = [1]
        r = [1]
        for i in range(len(A) - 1):
            l.append(A[i] * l[i])
            r.append(A[-i - 1] * r[i])
        return [l[j] * r[-j - 1] for j in range(len(A))]
