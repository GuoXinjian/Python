#
# @lc app=leetcode.cn id=1001 lang=python3
#
# [1001] 重复 N 次的元素
#
# https://leetcode-cn.com/problems/grid-illumination/description/
#
# algorithms
# Hard (24.76%)
# Total Accepted:    295
# Total Submissions: 1.1K
# Testcase Example:  '5\n[[0,0],[4,4]]\n[[1,1],[1,0]]'
#
# 在 N x N 的网格上，每个单元格 (x, y) 上都有一盏灯，其中 0 <= x < N 且 0 <= y < N 。
# 
# 最初，一定数量的灯是亮着的。lamps[i] 告诉我们亮着的第 i 盏灯的位置。每盏灯都照亮其所在 x 轴、y
# 轴和两条对角线上的每个正方形（类似于国际象棋中的皇后）。
# 
# 对于第 i 次查询 queries[i] = (x, y)，如果单元格 (x, y) 是被照亮的，则查询结果为 1，否则为 0 。
# 
# 在每个查询 (x, y) 之后 [按照查询的顺序]，我们关闭位于单元格 (x, y) 上或其相邻 8 个方向上（与单元格 (x, y)
# 共享一个角或边）的任何灯。
# 
# 返回答案数组 answer。每个值 answer[i] 应等于第 i 次查询 queries[i] 的结果。
# 
# 
# 
# 示例：
# 
# 输入：N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
# 输出：[1,0]
# 解释： 
# 在执行第一次查询之前，我们位于 [0, 0] 和 [4, 4] 灯是亮着的。
# 表示哪些单元格亮起的网格如下所示，其中 [0, 0] 位于左上角：
# 1 1 1 1 1
# 1 1 0 0 1
# 1 0 1 0 1
# 1 0 0 1 1
# 1 1 1 1 1
# 然后，由于单元格 [1, 1] 亮着，第一次查询返回 1。在此查询后，位于 [0，0] 处的灯将关闭，网格现在如下所示：
# 1 0 0 0 1
# 0 1 0 0 1
# 0 0 1 0 1
# 0 0 0 1 1
# 1 1 1 1 1
# 在执行第二次查询之前，我们只有 [4, 4] 处的灯亮着。现在，[1, 0] 处的查询返回 0，因为该单元格不再亮着。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 10^9
# 0 <= lamps.length <= 20000
# 0 <= queries.length <= 20000
# lamps[i].length == queries[i].length == 2
# 
# 
#
class Solution:
    def gridIllumination(self, N: int, lamps: 'List[List[int]]', queries: 'List[List[int]]') -> 'List[int]':
        dict_x, dict_y, dict_d1, dict_d2, res = {}, {}, {}, {}, []
        set_lamps = set()  # 加了这玩意才能过～～～
        for x, y in lamps:
            dict_x[x] = dict_x.get(x, 0)+1
            dict_y[y] = dict_y.get(y, 0)+1
            dict_d1[x+y] = dict_d1.get(x+y, 0)+1
            dict_d2[x-y] = dict_d2.get(x-y, 0)+1
            set_lamps.add((x, y))
        for x, y in queries:
            if dict_x.get(x, 0) or dict_y.get(y, 0) or dict_d1.get(x+y, 0) or dict_d2.get(x-y, 0):
                res.append(1)
            else:
                res.append(0)
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    loc_i, loc_j = x+i, y+j
                    if (loc_i, loc_j) in set_lamps:
                        dict_x[loc_i] -= 1
                        dict_y[loc_j] -= 1
                        dict_d1[loc_i+loc_j] -= 1
                        dict_d2[loc_i-loc_j] -= 1
                        set_lamps.remove((loc_i, loc_j))

        '''
        res=[]
        for q in queries:
            t=0
            for lamp in lamps:
                if q[0]==lamp[0] or q[1]==lamp[1] or sum(q)==sum(lamp) or q[0]-q[1]==lamp[0]-lamp[1]:
                    res.append(1)
                    t=1
                    break
            if t==0:
                res.append(0)
            l=-1
            while l<2:
                r=-1
                while r<2:
                    if [q[0]+l,q[1]+r] in lamps:lamps.remove([q[0]+l,q[1]+r])
                    r+=1
                l+=1
        '''
        return res

# s=Solution().gridIllumination(5,[[0,0],[0,4]],[[0,4],[0,1],[1,4]])
# print(s)
