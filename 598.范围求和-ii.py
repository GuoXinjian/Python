#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        for o in ops:
            if o[0]<m:
                m=o[0]
            if o[1]<n:
                n=o[1]
        return m*n

