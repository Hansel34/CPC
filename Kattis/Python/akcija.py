books = int(input())
prices = []
for _ in range(books):
    prices.append(int(input()))
count = 0
prices.sort(reverse=True)
price = 0
for book in prices:
    count +=1
    if count % 3 == 0:
        continue
    else:
        price+= book
print(price)
