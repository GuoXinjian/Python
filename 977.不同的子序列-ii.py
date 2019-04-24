#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 不同的子序列 II
#
class Solution:
    def func(self,x):
        return x**2
    def sortedSquares(self, A: List[int]) -> List[int]:
        A=list(map(abs,A))
        A.sort()
        return list(map(self.func,A))

