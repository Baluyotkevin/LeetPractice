class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        ans, temp = "", ""
        size = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                temp += s[j]
                if temp == temp[::-1] and size < len(temp):
                    ans = temp
                    size = len(temp)
            temp = ""
        return ans