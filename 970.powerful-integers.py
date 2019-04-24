#
# @lc app=leetcode.cn id=970 lang=python3
#
# [970] Powerful Integers
#
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> 'List[int]':
        res=set()
        i=0
        
        while True:
            if x**i>bound:
                break
            j=0
            while True:
                t=x**i+y**j
                if t<=bound:
                    res.add(t)
                    j+=1
                else:break
                if y==1:
                    break  
            i+=1
            if x==1:break
        return list(res)
# s=Solution().powerfulIntegers(2,1,10)
# print(s)