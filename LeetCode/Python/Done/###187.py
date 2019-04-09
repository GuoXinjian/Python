class Solution:
    def findRepeatedDnaSequences(self, s: str) -> 'List[str]':
        res=[]
        
        for i in range(len(s)-10):
            t=s[i:i+10]
            j=i+1
            while j<len(s)-9:
                if t==s[j:j+10]:
                    if t in res:pass
                    else:res.append(t)
                j+=1
            
        return res







s=Solution().findRepeatedDnaSequences("AAAAAAAAAAA")
print(s)