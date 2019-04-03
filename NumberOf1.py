# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n>=0:
            return bin(n).count('1')
        else:
            return bin(2**32+n).count('1')
