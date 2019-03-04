'''
我们正在玩一个猜数字游戏。 游戏规则如下：
我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
每次你猜错了，我会告诉你这个数字是大了还是小了。
你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

-1 : 我的数字比较小
 1 : 我的数字比较大
 0 : 恭喜！你猜对了！
示例 :

输入: n = 10, pick = 6
输出: 6
'''
def guess(num):
    n=1
    if num==n:
        return 0
    elif num>n:
        return -1
    else:return 1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        bot = 1
        top = n
        g = (bot + top)//2
        while guess(g) != 0:
            if guess(g) == 1:
                bot = g
            else:
                top = g
            g = (bot + top)//2
            if top - bot == 1:
                break
        if guess(g):
            return top
        return g


s=Solution()
res=s.guessNumber()
print(res)