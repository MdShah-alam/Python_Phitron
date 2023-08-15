
n = int(input())
coins = list(map(int, input().split()))

total_sum = sum(coins)
coins.sort(reverse=True)

taken_coins = 0
current_sum = 0

for coin in coins:
    current_sum += coin
    taken_coins += 1
    if current_sum > total_sum / 2:
        break

print(taken_coins)
