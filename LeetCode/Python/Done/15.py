'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

#1112ms
class Solution2:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res =[]
        i = 0
        for i in range(len(nums)):
            if i == 0 or nums[i]>nums[i-1]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] +nums[r]
                    if s ==0:
                        res.append([nums[i],nums[l],nums[r]])
                        l +=1
                        r -=1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s>0:
                        r -=1
                    else :
                        l +=1
        return res

#400ms
class Solution:
    def threeSum(self, nums):
        if len(nums)>=4:
            #if nums[0]>0 or nums[-1]<0:
            if min(nums)>0 or max(nums)<0:
                return []
        res=[]
        d=dict()
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
        posnum=[i for i in d  if i>0 ]
        negnum=[i for i in d  if i<0 ]
        if d.get(0,0)>2:
            res.append([0,0,0])
        if negnum==[] or posnum==[]:
            return res
        for i,x in enumerate(posnum):
            if d[x]>=2 and -2*x in d:
                res.append([x,x,-2*x])
            for y in posnum[i+1:]:
                if -(x+y) in d:
                    res.append([x,y,-x-y])
        for i,x in enumerate(negnum):
            if d[x]>1 and -2*x in d:
                res.append([x,x,-2*x])  
            for y in negnum[i+1:]:
                if -(x+y) in d:
                    res.append([x,y,-x-y])

        if 0 in d:
            for x in posnum:
                if -x in d:
                    res.append([x,0,-x])
        return res
        

nums=[-1,0,1,2,-1,-4]
S=Solution()
print(S.threeSum(nums))