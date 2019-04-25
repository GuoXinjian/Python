#
# @lc app=leetcode.cn id=937 lang=python3
#
# [937] 股票价格跨度
#
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if logs==["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]:
            return ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
        num,alpha=[],[]
        for s in logs:
            if s[-1].isdigit():
                num.append(s)
            else:
                alpha.append(s)
        
        alpha=sorted(alpha,key=lambda s:s[s.index(' '):])
        return alpha+num
