#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (45.99%)
# Total Accepted:    8.2K
# Total Submissions: 17.9K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# 
# 示例 1:
# 
# 输入: "hello"
# 输出: "holle"
# 
# 
# 示例 2:
# 
# 输入: "leetcode"
# 输出: "leotcede"
# 
# 说明:
# 元音字母不包含字母"y"。
# 
#
class Solution:
    def reverseVowels(self, s: str) -> str:
        res=[]
        r=[]
        t=[]
        for i in range(len(s)):
            res.append(s[i])
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                t.append(i)
                r.append(s[i])
        for a in t:
            res[a]=r.pop()
        return ''.join(res)



