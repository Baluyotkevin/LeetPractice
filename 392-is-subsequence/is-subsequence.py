class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # length = 0
        left = 0
        for i in range(len(t)):
            if left == len(s):
                break
            if s[left] == t[i]:
                # length+=1
                left+=1
        return len(s) == left
