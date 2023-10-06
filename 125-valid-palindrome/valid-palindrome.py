class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ''
        for letter in s.lower():
            if letter.isalnum():
                ans += letter
        return ans == ans[::-1]