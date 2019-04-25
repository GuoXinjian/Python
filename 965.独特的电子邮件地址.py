#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 独特的电子邮件地址
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        l = True
        r = True
        if root.left:
            l = root.val == root.left.val and self.isUnivalTree(root.left)
        if root.right:
            r = root.val == root.right.val and self.isUnivalTree(root.right)
        return l and r 

# class Solution:
#     def isUnivalTree(self, root: 'TreeNode') -> 'bool':
#         node_list = list()
#         node_list.append(root)
#         val = None
#         b = True
#         while node_list:
#             node = node_list.pop(0)
#             if not val or node.val == val:
#                 val = node.val
#                 b = True
#             else:
#                 b = False
#                 break
#             if node.left:
#                 node_list.append(node.left)
#             if node.right:
#                 node_list.append(node.right)
#         return b


