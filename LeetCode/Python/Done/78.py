'''

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''

class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        res=[[]]
        m=[[]]
        i=0
        l=len(nums)
        while i<l:
            t=[]
            for n in m:
                try:
                    j=nums.index(n[-1])+1
                except:
                    j=0
                for x in nums[j:]:
                    t.append(n+[x])
            res+=t
            m=t
            i+=1
        return res

nums=[1,2,3,4]
s=Solution()
res= s.subsets(nums)
print(res)