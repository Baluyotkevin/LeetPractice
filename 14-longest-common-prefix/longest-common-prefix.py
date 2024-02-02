class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        compare = strs[0]
        res = ""
        for i in range(len(compare)):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != compare[i]:
                    return res
            res+= compare[i]
        return res