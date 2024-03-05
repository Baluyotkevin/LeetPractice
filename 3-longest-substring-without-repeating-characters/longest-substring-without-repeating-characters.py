class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = ''
        ans = 0
        for r in range(len(s)):
            if s[r] in charSet:
                ans = max(ans, len(l))
                # Remove characters from the left until the repeating character
                while l[0] != s[r]:
                    charSet.remove(l[0])
                    l = l[1:]
                l = l[1:]  # Remove the repeating character itself
            charSet.add(s[r])
            l += s[r]
        ans = max(ans, len(l))  # Consider the length of the last substring
        return ans

