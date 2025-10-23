class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)!=2:
            ans=""
            for i in range(len(s)-1):
                value=(int(s[i])+int(s[i+1]))%10
                ans+=str(value)
            s=ans
        return True if s[0]==s[1] else False