class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        lowestPrevNum=prices[0]
        for i in range(1,len(prices)):
            if prices[i]-lowestPrevNum>maxProfit:
                maxProfit=prices[i]-lowestPrevNum
            elif prices[i]<lowestPrevNum:
                lowestPrevNum=prices[i]
        return maxProfit