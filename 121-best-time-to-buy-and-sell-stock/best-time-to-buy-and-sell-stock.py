class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # going to have two pointers
        # if pointer one is less than two then pointer one stays the same and pointer two increases other wise pointer one is now pointer two and pointer two increases
        # if right pointer
        # another variable will be our max
        left = 0
        right = 1
        max_sum = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            print(prices[left], prices[right])
            if prices[right] - prices[left] > max_sum:
                max_sum = prices[right] - prices[left]
            right+=1
        return max_sum

        