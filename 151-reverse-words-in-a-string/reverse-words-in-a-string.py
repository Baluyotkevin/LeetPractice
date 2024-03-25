class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        reverse = s.split()
        return ' '.join(reverse[::-1])