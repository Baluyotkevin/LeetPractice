class Solution:
    def isPalindrome(self, s: str) -> bool:
        # defining a new empty string variable
        # iterating through the string
        # check whether the element is an alphabet
        # then we can return that new variable string == reverse new varaible string
        res = ''
        for letter in s:
            if letter.isalnum():
                res += letter.lower()
        print(res)
        return res == res[::-1]