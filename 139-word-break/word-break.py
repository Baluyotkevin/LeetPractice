class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def check(s):
            if len(s) == 0:
                return True
            if s in memo: return memo[s]
            for word in wordDict:
                if s.startswith(word):
                    if check(s[len(word):]):
                        memo[s] = True
                        return True
            memo[s] = False
            return False
        return check(s)