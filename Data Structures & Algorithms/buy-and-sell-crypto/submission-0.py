class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        slow = 0
        max_val = 0

        for fast in range(n):
            if prices[fast] <= prices[slow]:
                slow = fast
            max_val = max(max_val, prices[fast] - prices[slow])
        return max_val
