#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 非重叠矩形中的随机点
#
class Solution:
    def hasGroupsSizeX(self, deck: 'List[int]') -> bool:
        S=set(deck)
        tmp=[]
        for s in S:
            tmp.append(deck.count(s))
        m = min(tmp)
        if m<2:return False
        i=2
        while i<=m:
            change=0
            for t in tmp:
                if t%i!=0:
                    change=1
                    break
            if change==0:
                return True
            i+=1
        return False

# s=Solution().hasGroupsSizeX([1,2,3,4,4,3,2,1])
# print(s)



