'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        try:
            l = len(strs[0])
        except:
            return ''
        res=''
        for i in range(l):
            try:
                tmp1 = strs[0][:i+1]
                for s in strs:
                    if s[:i+1]==tmp1:
                        tmp2=tmp1
                    else:
                        tmp2=''
                        break
                if tmp1==tmp2:
                    res = tmp1
            except:
                break
        return res

S=Solution()
s=["a"]
print(S.longestCommonPrefix(s))