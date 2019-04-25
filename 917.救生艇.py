#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 救生艇
#
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        tmp=[]
        res=[0]*len(S)
        for i in range(len(S)):
            if 97<=ord(S[i])<=122 or 65<=ord(S[i])<=90:
                tmp.append(S[i])
            else:
                res[i]=S[i]
        tmp=tmp[::-1]
        for i in tmp:
            for r in range(len(res)):
                if res[r]==0:
                    res[r]=i
                    break
        return ''.join(res)

# s=Solution().reverseOnlyLetters('ab-cd')
# print(s)

