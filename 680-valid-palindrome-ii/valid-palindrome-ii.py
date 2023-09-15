class Solution:
    def validPalindrome(self, s: str) -> bool:
        #we want to check if we delete any one character to see if its palindrome
        # loop through and see if you delete one character is it palindrome
        # if it is return true
        # otherwise return false
        left , right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                skipLeft, skipRight = s[left + 1:right + 1], s[left:right]
                return (skipLeft == skipLeft[::-1] 
                    or skipRight == skipRight[::-1])
            left+=1
            right-=1
        return True
            
