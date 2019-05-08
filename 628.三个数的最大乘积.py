#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if nums[1]<0:
            l=nums[0]*nums[1]
        else:l=0
        if nums[-3]>0:
            r=nums[-2]*nums[-3]
        else:r=0
        return max(l,r)*nums[-1]

