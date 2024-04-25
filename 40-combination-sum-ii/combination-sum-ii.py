class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(subset, pos, target):
            if target == 0:
                res.append(subset.copy())
            if target <= 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                subset.append(candidates[i])
                backtrack(subset, i + 1, target - candidates[i])
                subset.pop()
                prev = candidates[i]
        backtrack([], 0, target)
        return res