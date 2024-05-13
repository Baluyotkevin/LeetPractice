class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        res = []
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                res.append(i)
        return len(res)