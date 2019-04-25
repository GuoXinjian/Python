#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 最小差值 I
#
class Solution:
    def minDeletionSize(self, A: 'List[str]') -> int:
        res=0
        for i in range(len(A[0])):
            for j in range(len(A)-1):
                # print(A[j][i],A[j+1][i],ord(A[j][i]),ord(A[j+1][i]))
                if ord(A[j][i])>ord(A[j+1][i]):
                    res+=1
                    break
        return res
# s=Solution().minDeletionSize(["cba","daf","ghi"])
# print(s)
