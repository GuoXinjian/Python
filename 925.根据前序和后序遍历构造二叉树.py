#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 根据前序和后序遍历构造二叉树
#
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        tmp=name[0]
        for i in range(len(name)):
            try:
                if name[i]==name[i+1]:
                    tmp+=name[i+1]
                    continue
                else:
                    if typed[:len(tmp)]==tmp:
                        typed=typed[len(tmp):]
                        if typed:
                            while True:
                                if typed[0]==tmp[0]:
                                    typed=typed[1:]
                                    continue
                                else:
                                    break
                        tmp=name[i+1]
                    else:
                        return False
            except:
                if typed and len(typed)==typed.count(tmp[0]):return True
                else:return False


# s=Solution().isLongPressedName("pyplrz","ppyypllr")
# print(s)

