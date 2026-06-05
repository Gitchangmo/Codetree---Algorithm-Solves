n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
max_price = 0

for i in range(len(price)-1):
    for j in range(i+1, len(price)):
        if price[i] < price[j]:
            trade = price[j] - price[i]
            if trade > max_price:
                max_price = trade

print(max_price)