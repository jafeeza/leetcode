class Solution:
    def kthCharacter(self, k: int) -> str:
        intial=['a']
        while len(intial)<k:
            size=len(intial)
            for i in range(size):
                next_char=chr(ord('a')+((ord(intial[i]) - ord('a') + 1) % 26))
                intial.append(next_char)
        return intial[k-1]