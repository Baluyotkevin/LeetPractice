class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) < 2:
            return stones[0]
        sort = sorted(stones)
        first = sort[-1]
        second = sort[-2]
        if first != second:
            new = sort[:-2] + [abs(first - second)]
        if first == second:
            new = sort[:-2]
        return self.lastStoneWeight(new)