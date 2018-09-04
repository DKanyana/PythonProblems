#Write an efficient function that takes stock_prices and returns 
#the best profit I could have made 
#from one purchase and one sale of one share of Apple stock yesterday.

def get_max_profit(stock_prices):
    minprice = stock_prices[0]
    maxprofit = stock_prices[1]-stock_prices[0]
    
    for i in range(1,len(stock_prices)):
        currentprice = stock_prices[i]
        potentialprofit = currentprice - minprice
        maxprofit = max(potentialprofit,maxprofit)
        minprice = min(minprice,currentprice)
    return maxprofit
    
print(get_max_profit([10, 7, 5, 8, 11, 9]))