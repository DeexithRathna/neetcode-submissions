class Solution:
    def isPalindrome(self, s: str) -> bool:
        plain = ''.join(filter(str.isalnum, s)).lower()
        return plain[::-1] == plain
        