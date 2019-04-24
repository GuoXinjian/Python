#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] N 天后的牢房
#
# https://leetcode-cn.com/problems/rotting-oranges/description/
#
# algorithms
# Easy (45.61%)
# Total Accepted:    998
# Total Submissions: 2.2K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# 在给定的网格中，每个单元格可以有以下三个值之一：
# 
# 
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 
# 
# 每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
# 
# 返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
# 
# 
# 示例 2：
# 
# 输入：[[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
# 
# 
# 示例 3：
# 
# 输入：[[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] 仅为 0、1 或 2
# 
# 
#
# class Solution:
#     def orangesRotting(self, grid: 'List[List[int]]') -> int:
        # from copy import deepcopy
        # bad=[]
        # good=[]
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j]==2:
        #             bad.append([i,j])
        #         elif grid[i][j]==1:
        #             good.append([i,j])
        # res=0
        # while True:
        #     change=0
        #     if good:
        #         tmp_bad=deepcopy(bad)
        #         tmp_good=deepcopy(good)
        #         for b in tmp_bad:
        #             T=[[b[0]-1,b[1]],[b[0]+1,b[1]],[b[0],b[1]-1],[b[0],b[1]+1]]
        #             for t in T:
        #                 if t in good:
        #                     good.remove(t)
        #                     bad.append(t)
        #                     change=1
        #     if change==1:
        #         res+=1
        #     if change==0:
        #         if not good:
        #             return res
        #         else:
        #             return -1

class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        row, col = len(grid), len(grid[0])
        newturn = []
        # 扫描所有的烂橘子
        y = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    newturn.append((r,c))
                elif grid[r][c] == 1:
                    y += 1
        if y==0:
            return 0
        elif y>0 and len(newturn)==0:
            return -1
        
        cnt = 0
        while len(newturn)>0:
            cnt += 1
            nn = set()
            for r,c in newturn:
                if r>0 and grid[r-1][c]==1:
                    grid[r-1][c] = 2
                    nn.add((r-1,c))
                if r<row-1 and grid[r+1][c]==1:
                    grid[r+1][c] = 2
                    nn.add((r+1,c))
                if c>0 and grid[r][c-1]==1:
                    grid[r][c-1] = 2
                    nn.add((r,c-1))
                if c<col-1 and grid[r][c+1]==1:
                    grid[r][c+1] = 2
                    nn.add((r,c+1))
            newturn = nn
            # print(newturn)
            
        for rs in grid:
            for e in rs:
                if e == 1:
                    return -1
        return cnt -1
# s=Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
# print(s)

