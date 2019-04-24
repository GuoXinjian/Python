#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 煎饼排序
#
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        n=N
        if N==0:
            return 1 
        t=0
        while n>0:
            n=n>>1
            t+=1
        return 2**t-N-1