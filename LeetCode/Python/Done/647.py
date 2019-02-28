'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:

输入的字符串长度不会超过1000。
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        l=len(s)
        i=1
        while i<=l:
            for j in range(l-i+1):
                a=s[j:j+1]
                b=a[::-1]
                if s[j:j+1]==s[j:j+1]:res+=1
            i+=1
        return res


s=Solution()
res=s.countSubstrings('abc')
