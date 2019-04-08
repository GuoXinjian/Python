'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例:

输入: [2,1,5,6,2,3]
输出: 10

'''
class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> int:
        
        res=[]
        length=len(heights)
        if length==0:
            return 0
        for g in range(length):
            h=heights[g]
            l = g
            r = g
            while l>=0:
                if heights[l]>=h:
                    l-=1
                else:
                    break
            while r<length:
                if heights[r]>=h:
                    r+=1
                else:
                    break
            res.append(h*(r-l-1))

        return max(res)

s=Solution()
res=s.largestRectangleArea([2,1,5,6,2,3])
print(res)