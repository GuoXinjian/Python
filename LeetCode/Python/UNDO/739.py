'''
根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高的天数。如果之后都不会升高，请输入 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的都是 [30, 100] 范围内的整数。
'''

class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        l = len(T)
        res=[0]*l
        stack = []
        i = 0
        while i<l:
            if not stack or stack[-1]>=T[i]:
                stack.append(T[i])
            else:
                idx = T.index(stack.pop())
                T[idx] = 0
                res[idx] = i-idx
                continue
            i+=1
        l = len(stack)

        return res





S=Solution()
T=[73, 74, 75, 71, 69, 72, 76, 73]
print(S.dailyTemperatures(T))
