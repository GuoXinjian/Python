#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] 单值二叉树
#
class Solution:
    def largestSumAfterKNegations(self, A: 'List[int]', K: int) -> int:
        minus=[]
        plus=[]
        ta=sum(A)
        for a in A:
            if a<0:
                minus.append(a)
            else:
                plus.append(a)
        minus.sort()
        if K<=len(minus): return sum(A)-2*sum(minus[:K])
        else:
            k=K-len(minus)
            t=min(A,key=abs)
            t2=sum(A)-2*sum(minus)
            return sum(A)-2*sum(minus)-(k%2)*2*abs(t)

# class Solution:
#     def largestSumAfterKNegations(self, A: 'List[int]', K: int) -> int:
#         for i in range(K):
#             A[A.index(min(A))]*=-1
#         return (sum(A))

# s=Solution().largestSumAfterKNegations([5,6,9,-3,3],2)
# print(s)


