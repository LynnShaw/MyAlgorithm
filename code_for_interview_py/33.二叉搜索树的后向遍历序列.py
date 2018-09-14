# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence is None or len(sequence) == 0:
            return False
        return self.helper(sequence)

    def helper(self, sequence):

        # global i
        if sequence is None or len(sequence) == 0:
            return True

        for i in range(len(sequence)):
            if sequence[i] > sequence[-1]:
                break
        for j in range(i, len(sequence) - 1):
            if sequence[j] < sequence[-1]:
                return False
        # for right in sequence[i:-1]:
        #     if right < root:
        #         return False
        return self.helper(sequence[:i]) and self.helper(sequence[i:-1])

