#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0 :return '0'
        res=''
        t = '-' if num<0 else ''
        num=abs(num)
        while num:
            res = str(num%7) + res
            num=num//7
        return t+res

