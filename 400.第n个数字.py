#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第N个数字
#
# https://leetcode-cn.com/problems/nth-digit/description/
#
# algorithms
# Easy (30.86%)
# Total Accepted:    2.7K
# Total Submissions: 8.9K
# Testcase Example:  '3'
#
# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。
# 
# 注意:
# n 是正数且在32为整形范围内 ( n < 2^31)。
# 
# 示例 1:
# 
# 
# 输入:
# 3
# 
# 输出:
# 3
# 
# 
# 示例 2:
# 
# 
# 输入:
# 11
# 
# 输出:
# 0
# 
# 说明:
# 第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。
# 
# 
#
class Solution:
    def findNthDigit(self, n: int) -> int:
        

