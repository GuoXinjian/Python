#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (36.63%)
# Total Accepted:    4.2K
# Total Submissions: 11.4K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
# 
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
# 
# 说明：
# 
# 
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
# 
# 
# 示例 1:
# 
# 
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
# 
# 
# 示例 2:
# 
# 
# 输入:
# s: "abab" p: "ab"
# 
# 输出:
# [0, 1, 2]
# 
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
# 
# 
#
class Solution:
    def findAnagrams(self, s: str, p: str) -> 'List[int]':
        l=len(p)
        if len(s)<l:return []
        res=[]
        dic={}
        for q in p:
            if q in dic:
                dic[q]+=1
            else:
                dic[q]=1
        tmp={}
        for i in range(l):
            if s[i] in tmp:
                tmp[s[i]]+=1
            else:
                tmp[s[i]]=1
        if dic==tmp:
            res.append(0)
        j=0
        while j<len(s)-l:
            tmp[s[j]]-=1
            if tmp[s[j]]==0:
                del tmp[s[j]]
            if s[j+l] in tmp:
                tmp[s[j+l]]+=1
            else:
                tmp[s[j+l]]=1
            if tmp==dic:
                res.append(j+1)
            j+=1
        return res

s=Solution().findAnagrams("cbaebabacd","abc")
print(s)
