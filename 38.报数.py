#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (49.03%)
# Total Accepted:    27.2K
# Total Submissions: 55.4K
# Testcase Example:  '1'
#
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
# 
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
# 
# 注意：整数顺序将表示为一个字符串。
# 
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "1"
# 
# 
# 示例 2:
# 
# 输入: 4
# 输出: "1211"
# 
# 
#
class Solution:
    def __init__(self):
        self.dic = {1:'1',2:'11'}
        self.l=2
    def countAndSay(self, n: int) -> str:
        if self.l>n:
            return self.dic[n]
        
        while self.l<n:
            t=''
            count=1
            i=1
            while i<len(self.dic[self.l]):
                
                if self.dic[self.l][i]==self.dic[self.l][i-1]:
                    count+=1
                else:
                    t+=str(count)
                    t+=self.dic[self.l][i-1]
                    count=1
                    
                i+=1
            t+=str(count)
            t+=self.dic[self.l][i-1]
            self.l+=1
            self.dic[self.l]=t
            
        return self.dic[n]

s=Solution().countAndSay(4)
print(s)
