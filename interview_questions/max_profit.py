"""
You will be given a list of stock prices for a given day and your goal is to retum the maximum profit 
that could have been made by buying a stock at the given price and then selling the stock later on. For 
example if the input is: [45, 24, 35, 31, 40, 38, 11] then your program should return 16 because if 
you bought the stock at dolar 24 and sold it at dolar 40, a profit of dolar 16 was made and this is the 
largest pront that could be made.if no proft could have been made, retur -1.
megin: buy_price - 24, sell_price = 35, max_ pront = 11
"""

def stock_price(arr):
    max_profit = -1
    sell_price = 0
    buy_price = 0
    
    change_buy_index = True
    
    # loop through list 
    for i in range(0, len(arr)-1):
        #selling price
        sell_price = arr[i+1]
        
        #buying price = current price
        if change_buy_index:
            buy_price = arr[i]
            
        if sell_price < buy_price:
            change_buy_index = True
            continue #no profit
        else:
            temp_profit = sell_price - buy_price #positif = kar
            if temp_profit > max_profit:
                max_profit = temp_profit
            change_buy_index = False
    
    return max_profit

print(stock_price([23,66,18,345,98,105,45,12]))
        
        