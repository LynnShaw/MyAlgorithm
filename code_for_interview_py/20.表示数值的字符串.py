# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        hase = False
        hasp = False
        hass = False
        for i in range(len(s)):
            if s[i] == 'e' or s[i] == 'E':
                if hase:
                    return False
                else:
                    hase = True
                    if i == len(s) - 1:
                        return False
            elif s[i] == '+' or s[i] == '-':
                if hass:
                    if s[i - 1] != 'e' and s[i - 1] != 'E':
                        return False
                else:
                    hass = True
                    if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                        return False
            elif s[i] == '.':
                if hasp or hase:
                    return False
                else:
                    hasp = True
            else:
                if s[i] < '0' or s[i] > '9':
                    return False
        return True
