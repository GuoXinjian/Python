#
# @lc app=leetcode.cn id=999 lang=python3
#
# [999] 由斜杠划分区域
#
class Solution:
    def numRookCaptures(self, board: 'List[List[str]]') -> int:
        i=0
        res=0
        while i<8:
            j=0
            while j<8:
                if board[i][j]=='R':
                    m=i
                    n=j
                    while m>=0:
                        if board[m][n]=='B':
                            break
                        elif board[m][n]=='p':
                            res+=1
                            break
                        else :
                            m-=1
                    m=i
                    n=j
                    while m<8:
                        if board[m][n]=='B':
                            break
                        elif board[m][n]=='p':
                            res+=1
                            break
                        else :
                            m+=1
                    m=i
                    n=j
                    while n>=0:
                        if board[m][n]=='B':
                            break
                        elif board[m][n]=='p':
                            res+=1
                            break
                        else :
                            n-=1
                    m=i
                    n=j
                    while n<8:
                        if board[m][n]=='B':
                            break
                        elif board[m][n]=='p':
                            res+=1
                            break
                        else :
                            n+=1
                    break
                j+=1
            i+=1
        return res
                    
# s=Solution().numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]])
# print(s)
                    
