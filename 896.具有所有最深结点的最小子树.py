#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 具有所有最深结点的最小子树
#
class Solution:
    def isMonotonic(self, A: 'List[int]') -> bool:
        i=0
        t=0
        while i<len(A)-1:
            if A[i]==A[i+1]:pass
            elif A[i]<A[i+1]:
                if t==-1:
                    return False
                else:
                    t=1
            else:
                if t==1:
                    return False
                else:
                    t=-1
            i+=1
        return True

# s=Solution().isMonotonic([1,2,2,3])
# print(s)
