class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n=len(s)
        ans=[]
        while n%k!=0:
            s="".join([s,fill])
            n+=1
        c=[]
        for i in range(0,n,k):
            c=s[i:i+k]
            ans.append(c)
        return ans