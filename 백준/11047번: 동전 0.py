N, K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))

cnt = 0
for i in reversed(range(N)):
    cnt += K // coin[i]
    K = K % coin[i]

print(cnt)
