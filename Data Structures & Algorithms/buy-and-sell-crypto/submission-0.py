class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        promx = 0
        l=r=0
        while r<len(prices):
            if prices[r]-prices[l] <0:
                l=r
            if prices[r]-prices[l] >0:
                promx = max(promx,prices[r]-prices[l])
            r+=1
        return promx
        