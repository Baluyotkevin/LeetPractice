class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp, ans = "", ""
        size = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                temp+=s[j]
                if temp == temp[::-1] and len(temp) > size:
                    ans = temp
                    size = len(temp)
            temp = ""
        return ans