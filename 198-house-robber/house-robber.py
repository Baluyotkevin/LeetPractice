class Solution:
    def rob(self, nums: List[int]) -> int:
        [1, 2, 3, 1]
        rob1, rob2 = 0, 0
        for n in nums:
            # 1, 2
            # temp = (1 + 0, 0)
            # temp = (2 + 0, 1)
            # temp = (3 + 1, 2)
            # temp = (1 + 2, 4)
            temp = max(n + rob1, rob2)
            # rob1 = 0
            # rob1 = 1
            # rob1 = 2
            # rob1 = 4
            rob1 = rob2
            # rob2 = 1
            # rob2 = 2
            # rob2 = 4
            # rob2 = 4
            rob2 = temp
        return rob2