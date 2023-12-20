class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: return ""
        ans = ""
        for i in range(len(palindrome)):
            if palindrome[i] != 'a':
                ans+='a'
                ans+=palindrome[i+1:]
                if ans != ans[::-1]:
                    return ans
                else:
                    break
            ans+=palindrome[i]
        return palindrome[:-1]+'b'