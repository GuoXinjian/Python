#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 最大宽度坡
#
class Solution:
    def commonChars(self, A: 'List[str]') -> 'List[str]':
        dic={x:9999 for x in 'abcdefghijklmnopqrstuvwxyz'}
    

        for a in A:
            tmp={}
            for b in a:
                if b in tmp:
                    tmp[b]+=1
                else:
                    tmp[b]=1
            for d in dic:
                dic[d]=min(dic[d],tmp.get(d,0))
        res=[]
        for d in dic:
            res+=[d]*dic[d]
        return res
# s=Solution().commonChars(["bella","label","roller"])
# print(s)
