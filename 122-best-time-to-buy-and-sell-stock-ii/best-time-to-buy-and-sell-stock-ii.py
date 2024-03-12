class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        start = prices[0]
        len1 = len(prices)
        # [7, 1, 5, 3, 6, 4]
        for i in range(0, len1):
            # start = 7, 1, 5, 3 # prrices[i] = 1, 5, 3, 6
            # 7 !=< 1, 1 <= 5, 5 !=< 3, 3 <= 6
            #  total = 5, 5 + 6 = 11
            # 
            if start < prices[i]: 
                total += prices[i] - start
            start = prices[i]
        return total
                

