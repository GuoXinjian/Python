'''

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

'''

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0:
            return []
        dic = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res = ['']
        tmp1 = ['']
        for d in digits:
            tmp2=[]
            for w in dic[int(d)]:
                for t in res:
                    tmp2.append(t+w)
            res = tmp2
        return res

digits='23'
S=Solution()
d = S.letterCombinations(digits)
print(d)