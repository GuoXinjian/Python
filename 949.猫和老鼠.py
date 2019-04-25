#
# @lc app=leetcode.cn id=949 lang=python3
#
# [949] 猫和老鼠
#
class Solution:
    def largestTimeFromDigits(self, A: 'List[int]') -> str:
        
        A.sort(reverse=True)
        if A[1]==0:
            if A[0]>2:return '0'+str(A[0])+':00'
            else: return str(A[0])+'0:00'
        if A[2]==0:
            if A[1]==1 and A[0]<3:return str(A[0])+'1:00'
            elif A[1]==1 and A[0]<5:return '1'+str(A[0])+':00'
            elif A[1]==2 and A[0]<4:return '2'+str(A[0])+':00'
            elif A[1]<6:return '0'+str(A[0])+':'+str(A[1])+'0'
            else: return '0'+str(A[0])+':0'+str(A[1])
        h1=[]
        h2=[]
        m1=[]
        m2=[]
        for a in A:
            if a<3: h1.append(a)
            if a<4: h2.append(a)
            if a<6: m1.append(a)
            m2.append(a)
        if len(h1)==0:return ''
        if len(h2)>1 and len(m1)>2:
            h2.remove(h1[0])
            m1.remove(h1[0])
            m2.remove(h1[0])
            m1.remove(h2[0])
            m2.remove(h2[0])
            m2.remove(m1[0])

            return str(h1[0])+str(h2[0])+':'+str(m1[0])+str(m2[0])
        elif len(h2)==1 and len(m1)==1:
            return ''
        elif len(h2)==1 and len(m1)>1:
            m2.remove(h1[0])
            m2.remove(m1[0])
            return str(h1[0])+str(m2[0])+':'+str(m1[0])+str(m2[1])
        

# s=Solution().largestTimeFromDigits([0,4,0,0])
# print(s)
