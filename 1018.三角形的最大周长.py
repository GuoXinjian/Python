#
# @lc app=leetcode.cn id=1018 lang=python3
#
# [1018] 三角形的最大周长
#
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:

        res=[]
        tmp=0
        for a in A:
            tmp=tmp*2+a
            if tmp%5==0:
                res.append(True)
            else:
                res.append(False)
        return res