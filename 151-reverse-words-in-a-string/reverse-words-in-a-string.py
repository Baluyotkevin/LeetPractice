class Solution:
    def reverseWords(self, s: str) -> str:
        reverse = s.split()
        return ' '.join(reverse[::-1])