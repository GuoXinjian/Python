#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#
class Solution:
    def findErrorNums(self, nums: 'List[int]') -> 'List[int]':
        i=0
        l=None
        r=None
        nums.sort()
        num=[n for n in range(1,len(nums)+1)]
        while i <len(nums)-1:
            if nums[i]==num[i]:i+=1
            elif nums[i]>num[i]:
                r=num[i]
                num.pop(i)
            else :
                l=nums[i]
                nums.pop(i)
            
        if l and r:return [l,r]




s=Solution().findErrorNums([1,2,2,4])
print(s)






