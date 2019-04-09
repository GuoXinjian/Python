'''

给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

示例:
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

输入: S = "3z4"
输出: ["3z4", "3Z4"]

输入: S = "12345"
输出: ["12345"]
注意：

S 的长度不超过12。
S 仅由数字和字母组成。

'''

class Solution:
    def letterCasePermutation(self, S: str) -> 'List[str]':
        res=['']
        for s in S:
            if s.isdigit():
                tmp=[]
                for r in res:
                    tmp.append(r+s)
                res=tmp
            else: 
                tmp=[]
                for r in res:
                    tmp.append(r+s.lower())
                    tmp.append(r+s.upper())
                res=tmp
        return res

s=Solution()
res=s.letterCasePermutation("a1b2")
print(res)