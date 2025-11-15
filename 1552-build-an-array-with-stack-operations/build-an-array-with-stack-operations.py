class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s=[]
        res=[]
        i=1
        while i<n+1 and len(s)!=len(target):
            s.append(i)
            res.append("Push")
            if i not in target:
                res.append("Pop")
                s.remove(i)
            i+=1
        return res