#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#
class Solution:
    def findRelativeRanks(self, nums: 'List[int]') -> 'List[str]':
        dic={}
        A=sorted(nums,reverse=True)
        b=["Gold Medal", "Silver Medal", "Bronze Medal"]
        i=1
        for a in A:
            if i<4:
                dic[a]=b[i-1]
            else:
                dic[a]=str(i)
            i+=1
        res=[]
        for n in nums:
            res.append(dic[n])

        return res
            
# s=Solution().findRelativeRanks([10,3,8,9,4])        
# print(s)  

