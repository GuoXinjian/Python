'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

Given a string, find the length of the longest substring without repeating characters.

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp1=''
        tmp2=''
        for word in s:
            i = tmp2.find(word)
            if i == -1:
                tmp2 += word
            else:
                tmp2 = tmp2[i+1:]
                tmp2 += word
            if len(tmp2)>=len(tmp1):
                tmp1=tmp2
        return len(tmp1)
