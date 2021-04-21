"""
"""
n = int(input())
k = list(map(int, input().split()))

# DT 테이블 초기화
# d[1] = 첫 번째 얻은 식량 / d[2] = 두 번째 얻은 식량 / d[3] = 세 번째 얻은 식량(누적) / ...
d = [0] * n

d[0] = k[0]
d[1] = max(k[0], k[1])
# bottom-up 다이나믹 프로그래밍
for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + k[i])

print(d[n-1])
