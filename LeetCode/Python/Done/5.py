'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp=''
        res=''
        l=len(s)
        i=0
        if len(s)<2:
            return s
        while i<l-1:
            tmp = s[i]
            j=1
            while i>=j and i+j<l:
                if s[i-j]==s[i+j]:
                    tmp = s[i-j:i+j+1]
                else:
                    break
                j+=1
            if len(tmp)>len(res):
                res=tmp
            if s[i]==s[i+1]:
                tmp = s[i:i+2]
                j=1
                while i>=j and i+j+1<l:
                    if s[i-j]==s[i+j+1]:
                        tmp = s[i-j:i+j+2]
                    else:
                        break
                    j+=1
                if len(tmp)>len(res):
                    res=tmp
            i+=1
        return res

s='ccc'
S=Solution()
print(S.longestPalindrome(s))