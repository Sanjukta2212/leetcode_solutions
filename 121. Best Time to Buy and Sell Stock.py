def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        first_price=prices[0]
        profit=0
        for sec_price in prices[1:]:
            if sec_price>first_price:
                diff=sec_price-first_price
                profit=max(profit, diff)
            else:
                first_price=sec_price
        return(profit)

if __name__=="__main__":
    head=[7,1,5,3,6,4]
    maxProfit(head)