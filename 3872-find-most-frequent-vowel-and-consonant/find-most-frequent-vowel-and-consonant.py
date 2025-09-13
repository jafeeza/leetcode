class Solution:
    def maxFreqSum(self, s: str) -> int:
        mp=Counter(s)
        vowel=max((mp[ch] for ch in mp if ch in "aeiou"),default=0)
        c=max((mp[ch] for ch in mp if ch not in "aeiou"),default=0)
        return vowel+c