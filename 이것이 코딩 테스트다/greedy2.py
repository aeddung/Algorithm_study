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

# m이 10,000 이상일 때 위의 방법으로 구현하려면 시간 초과
# 수학적으로 계산해보자.(반복되는 패턴을 찾아보기)
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수
# int(m / (k + 1))은 특정한 수열 형태가 반복되는 횟수
# ex) 6 + 6 + 6 + 5 / 6 + 6 + 6 + 5 / 6 
# m이 k+1에 의해 나누어 떨어지지 않는 경우 나머지를 더해준다.
num_of_first = int(m / (k + 1)) * k + (m % (k + 1))

result = num_of_first * first + int(m / (k + 1)) * second # int(m / (k + 1)) = m - num_of_first

print(result)
