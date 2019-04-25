#
# @lc app=leetcode.cn id=942 lang=python3
#
# [942] 超级回文数
#
class Solution:
    def diStringMatch(self, S: str) -> 'List[int]':
        N=len(S)
        res=[n for n in range(N+1)]
        i=0
        while i < N:
            if i==-1:
                i+=1
            if S[i]=='I':
                if res[i]<res[i+1]:
                    pass
                else:
                    res[i],res[i+1]=res[i+1],res[i]
                    i-=2

            else:
                if res[i]>res[i+1]:
                    pass
                else:
                    res[i],res[i+1]=res[i+1],res[i]
                    i-=2

            i+=1
        return res

# s=Solution().diStringMatch("D")
# print(s)
