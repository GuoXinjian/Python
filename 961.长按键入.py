#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 长按键入
#
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dic={}
        for a in A:
            if a in dic:
                return a
            else:
                dic[a]=1

