class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        compare = strs[0]
        res = ""
        for i in range(len(compare)):
            for s in strs:
                if i == len(s) or s[i] != compare[i]:
                    return res
            res+= compare[i]
        return res