'''
如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
以下数列不是等差数列。

1, 1, 2, 5, 7
 

数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

如果满足以下条件，则称子数组(P, Q)为等差数组：

元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

函数要返回数组 A 中所有为等差数组的子数组个数。

 

示例:

A = [1, 2, 3, 4]

返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。
'''
#64ms
class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)<3:
            return 0
        B=[]
        C=[1,]
        res = 0
        for i in range(1,len(A)):
            B.append(A[i]-A[i-1])
        for i in range(1,len(B)):
            if B[i]==B[i-1]:
                C[-1]+=1
            else:
                C.append(1)
        for i in C:
            res+=(i*(i-1))//2
        return res


#36ms
class Solution2:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # res = 0
        n = len(A)
        if n < 3:
            return 0
        else:
            dp = [0] * n
            if A[2] -A[1] == A[1] -A[0]:
                dp[2] = 1
            res = dp[2]
            for i in range(3, n):
                if A[i] - A[i-1] == A[i-1] - A[i-2]:
                    dp[i] = 1 + dp[i-1]
                res += dp[i]
            return res