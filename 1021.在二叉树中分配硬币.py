#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 在二叉树中分配硬币
#
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res=[]
        tmp=''
        t=0
        for s in S:
            if s=='(':
                tmp+=s
                t+=1
            else:
                tmp+=s
                t-=1
            if t==0:
                res.append(tmp)
                tmp=''
        res2=[]
        for r in res:
            res2.append(r[1:-1])
        return ''.join(res2)
