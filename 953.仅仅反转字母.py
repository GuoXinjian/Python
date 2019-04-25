#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 仅仅反转字母
#
class Solution:
    def isAlienSorted(self, words: 'List[str]', order: str) -> bool:
        dic={}
        t=0
        for o in order:
            dic[o]=t
            t+=1
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                try:
                    if dic[words[i][j]]<dic[words[i+1][j]]:
                        break
                    elif dic[words[i][j]]>dic[words[i+1][j]]:
                        return False
                except:
                    return False
        return True
# s=Solution().isAlienSorted( ["word","world","row"],"worldabcefghijkmnpqstuvxyz")
# print(s)