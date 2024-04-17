class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        right = 0
        satisfy = 0
        for i in range(len(s)):
            if g[right] <= s[i]:
                right += 1
                satisfy += 1
            if right == len(g):
                break
        return satisfy
