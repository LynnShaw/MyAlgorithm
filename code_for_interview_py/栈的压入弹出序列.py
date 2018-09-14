# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        tmp = []
        while popV:
            if pushV and pushV[0] == popV[0]:
                popV.pop(0)
                pushV.pop(0)
            elif tmp and tmp[-1] == popV[0]:
                popV.pop(0)
                tmp.pop()
            elif pushV:
                tmp.append(pushV.pop(0))
            else:
                return False
        return True
