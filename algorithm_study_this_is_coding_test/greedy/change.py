n = 1260

coins = [500, 100, 50, 10]

result = []

for coin in coins:
    result.append(n // coin)
    n = n % coin

print(result)