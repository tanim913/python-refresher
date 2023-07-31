class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_prof = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                '''
                only if we buy at low price and sell at high price
                we can make profit. so everytime that happens we calculate
                the profit and store the max one
                '''
                profit = prices[right] - prices[left]
                max_prof = max (profit, max_prof)
            else: # prices[left] >= prices[right]
                '''
                when we buy high and sell low or equal price, 
                we made a loss or made no profit
                so we need to start from the beginning .so we make the
                right pointer as left
                '''
                left = right
            right += 1 # and no matter what happens, time moves forward and so the right pointer 
        return max_prof
    
    ''' ***********best-time-to-buy-and-sell-stock-ii*******************
        class Solution:
            def maxProfit(self, prices: List[int]) -> int:
                profit = 0
                for i in range(1, len(prices)):
                *start from 1 so that there would be a value on 0
                and 0th index does not have a previous value
                    if prices[i] > prices[i-1]: #imagine picture
                        profit += (prices[i] - prices[i-1])
                return profit
    '''