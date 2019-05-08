#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        ori=word[:]
        return ori==word.upper() or ori==word.lower() or ori==word.capitalize()

