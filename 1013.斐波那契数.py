#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 斐波那契数
#
# https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum/description/
#
# algorithms
# Easy (41.36%)
# Total Accepted:    1K
# Total Submissions: 2.5K
# Testcase Example:  '[0,2,1,-6,6,-7,9,1,2,0,1]'
#
# 给定一个整数数组 A，只有我们可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
# 
# 形式上，如果我们可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ...
# + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。
# 
# 
# 
# 示例 1：
# 
# 输出：[0,2,1,-6,6,-7,9,1,2,0,1]
# 输出：true
# 解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# 
# 
# 示例 2：
# 
# 输入：[0,2,1,-6,6,7,9,-1,2,0,1]
# 输出：false
# 
# 
# 示例 3：
# 
# 输入：[3,3,6,5,-2,2,5,1,-9,4]
# 输出：true
# 解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= A.length <= 50000
# -10000 <= A[i] <= 10000
# 
# 
#
class Solution:
    def canThreePartsEqualSum(self, A: 'List[int]') -> bool:
        S = sum(A)
        if S%3!=0:
            return False
        l=len(A)
        s=S//3
        tmp=A[0]
        i=1
        j=0
        while i<l:
            if tmp==s:
                j=i
                break
            else:
                tmp+=A[i]
                i+=1
        if j==0:return False
        tmp=0
        while j<l:
            tmp+=A[j]
            j+=1
            if tmp==s:
                return True
        return False
s=Solution().canThreePartsEqualSum([12,-4,16,-5,9,-3,3,8,0])
print(s)
