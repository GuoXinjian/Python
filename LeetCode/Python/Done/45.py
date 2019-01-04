'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。
'''


#92ms
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        i=0
        count=0
        while i < l-1:
            tmp=0
            for n in range(1,nums[i]+1):
                if i+n>=l-1:
                    return count+1
                if n+nums[i+n]>tmp:
                    tmp=n+nums[i+n]
                    t=n
            i+=t
            count+=1
        return count

#52ms
class Solution2:
    def jump(self, nums):
        """
        52ms 100%
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return 0
        if len(set(nums)) == 1:  # 特殊情况加速判断
            return (len(nums) - 2) // nums[0] + 1
        
        steps = num_where = 0
        last = max_range = 0
        for i in nums:
            if last < num_where + i:
                last = num_where + i
            if num_where == max_range and num_where + 1 < l:
                max_range = last
                steps += 1
            num_where = num_where + 1
        return steps
        
nums = [1,2,3]
s=Solution()
print(s.jump(nums))