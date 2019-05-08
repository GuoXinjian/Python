#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] Fibonacci Number
#
class Solution:
    def fib(self, N: int) -> int:
        lis =[]
        for i in range(31):
            if i ==0:#第1,2项 都为1
                lis.append(0)
            elif i ==1:
                lis.append(1)
            else:
                lis.append(lis[i-2]+lis[i-1])
        return lis[N]