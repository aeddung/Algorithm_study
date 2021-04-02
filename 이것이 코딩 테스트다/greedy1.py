"""
동전 종류가 500원, 100원, 50원, 10원이 있고, 
N원의 거스름돈을 돌려주어야 하는 상황에서,
사용하는 동전의 최소 개수는?
"""

n = 1260
count = 0

coin_types = [500, 100, 50, 10]
for coin in coin_types:
  count += n // coin
  n = n % coin

print(count)
