'''

给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''

class Solution:
    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        res=[[]]
        t=[[]]
        i=0
        while i<len(nums):
            t2=t
            t=[]
            for r in t2:
                
                x=0
                l=i+x
                while l<len(nums):
                    tmp = r+[nums[l]]
                    t.append(tmp)
                    l+=1
                x+=1
            i+=1
            res+=t
        return set(res)

s=Solution()
res=s.subsetsWithDup([1,2,2])
print(res)