class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        l = 0
        for r in range(len(prices)):
            cur_pro = prices[r] - prices[l]
            if cur_pro > max_pro:
                max_pro = cur_pro
            if prices[r] < prices[l] and r < len(prices) - 1:
                l = r
        return max_pro