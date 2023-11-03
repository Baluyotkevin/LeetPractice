class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        ans = 0
        # string '' + 'a' = a
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+= 1
            charSet.add(s[r])
            ans = max(ans, r - l + 1)
        return ans
