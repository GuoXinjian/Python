'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。


'''

class Solution:
    def minSubArrayLen(self, s: int, nums: 'List[int]') -> int:
        l = 0
        r = 0 
        length=len(nums)
        res=[0,]
        a=0
        while r<length+1:
            if a<s and r<length:
                a+=nums[r]
                r+=1
            elif a>=s:
                res.append(r-l)
                a-=nums[l]
                l+=1
            else:
                r+=1
        return 0 if len(res)==1 else min(res[1:])


s=Solution()
res = s.minSubArrayLen(7,[2,3,1,2,4,3])
print(res)