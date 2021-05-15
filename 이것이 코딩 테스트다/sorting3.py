"""
하나의 수열에는 다양한 수가 존재한다. 큰 수부터 작은 수의 순서로 정렬해라.
수의 개수는 N으로 주어진다.
1 <= N <= 500, 1 <= 하나의 수 <= 100,000
"""
n = int(input())
data = []
for _ in range(n):
  data.append(input())

data.sort(reverse=True)
print(' '.join(data))
