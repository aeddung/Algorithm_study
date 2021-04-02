# 공백으로 n, m, k 구분해서 입력
# map()으로 integer 변환
n, m, k = map(int, input().split())

# n개의 자연수 입력(공백 구분)
data = list(map(int, input().split()))

data.sort()
# 가장 큰 수
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
  for i in range(k):
    if m == 0: # 더하다가 m 번 채우면 for문 종료
      break
    result += first
    m -= 1

  # m 번 다 더했으면 while문 종료
  if m == 0:
    break

  # k번 다 더했으면 두 번째로 작은 수 더하고 다시 for문 시작
  result += second
  m -= 1

print(result)
