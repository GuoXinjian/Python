'''
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:

输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5
 

示例2:

输入: 3
输出: False

'''
import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        j = int(math.sqrt(c))
        i = 0
        while i <= j:
            total = i * i + j * j
            if total > c:
                j = j - 1
            elif total < c:
                i = i + 1
            else:
                return True
        return False


class Solution2(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c <= 2:
            return True
        while c % 2 == 0:
            c = c // 2
        p = 3
        while p * p <= c:
            index = 0
            while c % p == 0:
                index += 1
                c = c // p
            if (p % 4 == 3) and (index % 2 == 1):
                return False
            p += 2
        return c % 4 == 1