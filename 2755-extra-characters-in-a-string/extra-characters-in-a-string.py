class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # convert to hash so that look up is faster
        words = set(dictionary)
        memo = {}
        def dfs(i):
            if i == len(s):
                return 0
            if i in memo:
                return memo[i]
            res = 1 + dfs(i + 1) # skip the character and a character is added  because we skipped it
            for j in range(i, len(s)):
                if s[i:j + 1] in words:
                    res = min(res, dfs(j + 1))
            memo[i] = res
            return res
        
        return dfs(0)