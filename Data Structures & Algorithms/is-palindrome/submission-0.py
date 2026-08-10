class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_1 = "".join(c.lower() for c in s if c.isalnum())
        return s_1 == s_1[::-1]