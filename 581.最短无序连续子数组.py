#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#
class Solution(object):
    # def findUnsortedSubarray(self, nums):
    #     max_num = 0 - 1 << 31 # This is the same as multiplying x by 2**y.
    #     min_num = 1 << 31 - 1
    #     right = left = 0
    #     for i in range(len(nums)): # 顺序扫描，找到最大值
    #         if max_num > nums[i]:
    #             right = i # 如果最大值小于当前值，那么当前值需要排序，包括在子数组内
    #         else:
    #             max_num = nums[i] # 递增时不断更新最大值
    #     if right == 0: # 如果扫描完毕right没有移动，即为递增数组
    #         return 0
    #     for i in range(len(nums) - 1, -1, -1): # 逆序扫描，找到最小值
    #         if min_num < nums[i]:
    #             left = i
    #         else:
    #             min_num = nums[i]
    #     return right - left + 1 

    def findUnsortedSubarray(self, nums):
        if nums == sorted(nums):
            return 0
        while nums[-1]==max(nums):
            nums.pop()
        while nums[0]== min(nums):
            nums.pop(0)
        return len(nums)