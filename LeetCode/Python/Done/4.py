'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=[]
        l1 = len(nums1)
        l2 = len(nums2)
        i = 0
        j = 0
        #归并排序法
        while i < l1+1 and j<l2+1:
            if i+j==l1+l2:
                break
            elif i==l1 :
                nums.append(nums2[j])
                j+=1
            elif j==l2 :
                nums.append(nums1[i])
                i+=1
            elif nums1[i]>=nums2[j]:
                nums.append(nums2[j])
                j+=1
            else:
                nums.append(nums1[i])
                i+=1
        if (l1+l2)%2 ==0:
            return float((nums[(l1+l2)//2-1]+nums[(l1+l2)//2])/2)
        else:
            return float(nums[(l1+l2)//2])

