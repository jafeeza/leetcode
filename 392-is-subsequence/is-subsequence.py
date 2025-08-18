class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sl=len(s)
        tl=len(t)
        if sl==0:
            return True
        dp=[[0]*(tl+1) for _ in range(sl+1)]
        for col in range(1,tl+1):
            for row in range(1,sl+1):
                if s[row-1]==t[col-1]:
                    dp[row][col]=dp[row-1][col-1]+1
                else:
                    dp[row][col]=max(dp[row-1][col],dp[row][col-1])
            if dp[sl][col]==sl:
                return True
        return False