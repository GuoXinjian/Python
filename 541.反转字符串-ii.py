#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ''
        loop = int(len(s) / (2*k))
        for i in range(loop):
            result += (s[i*2*k: i*2*k+k][::-1] + s[i*2*k+k: i*2*k+2*k])
        if len(s[loop*2*k:]) >= k:
            result += (s[loop*2*k:loop*2*k+k][::-1] + s[loop*2*k+k:])
        else:
            result += s[loop*2*k:][::-1]
        return result