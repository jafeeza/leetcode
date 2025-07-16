class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i,j):
            left=i
            right=j-1
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        for l in range(len(s),0,-1):
            for sta in range(len(s)-l+1):
                if check(sta,sta+l):
                    return s[sta:sta+l]
        return ""