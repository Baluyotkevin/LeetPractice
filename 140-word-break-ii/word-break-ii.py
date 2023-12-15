class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        def helper(s):
            if s in memo: return memo[s]
            if len(s) == 0: return [[]]
            res = []
            for word in wordDict:
                if s.startswith(word):
                    suffix = s[len(word):]
                    suffixWays = helper(suffix)
                    targetWays = [[word] + way for way in suffixWays]
                    res.extend(targetWays)
            memo[s] = res
            return res
        return [' '.join(sentence) for sentence in helper(s)]
                        
