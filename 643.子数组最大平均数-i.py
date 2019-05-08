#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmp=sum(nums[:k])
        m=tmp
        for i in range(len(nums)-k):
            tmp+=nums[i+k]-nums[i]
            if tmp>m:
                m=tmp
        return  m/k

