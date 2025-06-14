class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap = {']':'[' , ')':'(' , '}':'{'}
        stack = []

        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                if stack and stack[-1]==hashmap[char]:
                    stack.pop()
                else:
                    return False
        return not stack