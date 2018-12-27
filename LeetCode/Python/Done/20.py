'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
'''

#108ms
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = ['()','{}','[]']
        while len(s)!=0:
            t=s
            for a in arr:
                if a in s:
                    s=s.replace(a,'')
            if t==s:
                return False
        return True

#40ms
class Solution2:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        wrong_map = {')':'(', ']':'[', '}':'{'}
        
        for c in s:
            if c not in wrong_map:
                stack.append(c)
            elif not stack or wrong_map[c] != stack.pop():
                return False
        
        return not stack

s="([)]"
S=Solution2()
D=S.isValid(s)