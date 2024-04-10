class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # we can create a dict to keep track of whats in the nums
        # can get the max and the min
        # bruteforce solution
        check = {}
        res = []
        max_num = len(grid) * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] not in check:
                    check[grid[i][j]] = 1
                else:
                    check[grid[i][j]] += 1
        sort = dict(sorted(check.items(), key=lambda num: num[0]))
        missing = 0
        repeat = 0
        for num, count in sort.items():
            if count == 2:
                repeat = num
        while max_num > 0:
            if max_num not in sort:
                missing = max_num
            max_num -= 1
        return [repeat, missing]


            