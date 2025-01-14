cash = int(input())

stock_price = list(map(int, input().split()))

# print(cash) #100
# print(stock_price) #[10, 20, 23, 34, 55, 30, 22, 19, 12, 45, 23, 44, 34, 38]

def buy_stock(stock_price, cash):
    i = 0
    while (stock_price * i <= cash):
        i += 1
    i -= 1
    return cash-(stock_price*i), i

# remaining_cash, held_stock = buy_stock(stock_price[0], cash)
# print(remaining_cash)
# print(held_stock)
def long(stock_price, cash):
    long_stock = 0
    for i in stock_price:
        remaining_cash, held_stock = buy_stock(i, cash)
        cash = remaining_cash
        long_stock += held_stock
    return cash+long_stock*stock_price[-1]
# print('장투',long(stock_price, cash))

def short(stock_price, cash):
    short_stock = 0
    for i in range(14):
        if i >= 3:
            # print(i,'iiiii')
            if (stock_price[i-3] > stock_price[i-2] > stock_price[i-1]): #3일 연속 하락
                remaining_cash, held_stock = buy_stock(stock_price[i], cash)
                cash = remaining_cash
                short_stock += held_stock
                # print('하락장:',stock_price[i], cash, short_stock)
            elif (stock_price[i-3] < stock_price[i-2] < stock_price[i-1]) and short_stock > 0: #3일 연속 상승
                cash += short_stock * stock_price[i]
                short_stock = 0
                # print('상승장:',i,stock_price[i])
    return cash + (short_stock * stock_price[-1])
# print('단타',short(stock_price, cash))
long = long(stock_price, cash)
short = short(stock_price, cash)
if long > short:
    print('BNP')
elif long < short:
    print('TIMING')
else:
    print('SAMESAME')

