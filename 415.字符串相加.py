#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (44.42%)
# Total Accepted:    6.3K
# Total Submissions: 14.2K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 
# 注意：
# 
# 
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
# 
# 
#
def toint(x):
    if x:
        return int(x)
    else:
        return 0
class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        
        res=''
        if len(num1)<=len(num2):
            num1,num2=num2,num1
        r=0
        while num1:
            t=toint(num2[-1:])+toint(num1[-1:])
            res=str((t%10+r)%10)+res
            r=(t+r)//10
            num2=num2[:-1]
            num1=num1[:-1]
        if r!=0:
            res=str(r)+res
        return res
s=Solution().addStrings('9','99')
print(s)

