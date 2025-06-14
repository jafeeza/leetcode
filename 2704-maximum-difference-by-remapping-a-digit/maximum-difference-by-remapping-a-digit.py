class Solution:
    def minMaxDifference(self, num: int) -> int:
        s=str(num)
        t=s
        po=0
        while po<len(s) and s[po]=="9":
            po+=1
        if po<len(s):
            s=s.replace(s[po],"9")
        t=t.replace(t[0],"0")
        return int(s)-int(t)