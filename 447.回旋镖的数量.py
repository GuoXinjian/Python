#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#
# https://leetcode-cn.com/problems/number-of-boomerangs/description/
#
# algorithms
# Easy (53.72%)
# Total Accepted:    3.6K
# Total Submissions: 6.8K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# 给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k
# 之间的距离相等（需要考虑元组的顺序）。
# 
# 找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。
# 
# 示例:
# 
# 
# 输入:
# [[0,0],[1,0],[2,0]]
# 
# 输出:
# 2
# 
# 解释:
# 两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
# 
# 
#
class Solution:
    def numberOfBoomerangs(self, points: 'List[List[int]]') -> int:
        
        res=0
        for i in range(len(points)):
            j=0
            dic={}
            while j<len(points):
                l = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                if l in dic:
                    dic[l]+=1
                else:dic[l]=1
                j+=1
            for k,v in dic.items():
                res+=v*(v-1)
        return res
# s=Solution().numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])
# print(s)


