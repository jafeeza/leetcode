class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        re=-1
        if len(haystack) < len(needle):
            return -1
        for i in range(0,len(haystack)):
            if haystack[i:i+len(needle)]==needle:
                return i
        return re