# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        ll = len(rotateArray)
        if ll == 0:
            return 0
        l, r = 0, ll-1
        mid = 0
        while rotateArray[l] >= rotateArray[r]:
            if l == r-1:
                return rotateArray[r]
            mid = (l + r) // 2
            if (rotateArray[mid] == rotateArray[l] and rotateArray[l] == rotateArray[r]):
                return min(rotateArray)
            if rotateArray[mid] >= rotateArray[l]:
                l = mid
            else:
                r = mid

        return rotateArray[mid]
