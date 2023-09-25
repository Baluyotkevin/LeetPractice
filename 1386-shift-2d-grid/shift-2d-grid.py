class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        def pos_to_val(r, c):
            return r * n + c
        def val_to_pos(v):
            return [v // n, v % n]
        
        res = [[0] * n for i in range(m)]
        for r in range(m):
            for c in range(n):
                new_val = (pos_to_val(r, c) + k) % (m * n)
                new_r, new_c = val_to_pos(new_val)
                res[new_r][new_c] = grid[r][c]

        return res