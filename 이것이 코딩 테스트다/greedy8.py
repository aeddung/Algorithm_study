"""
N개의 동전이 있을 때, 이를 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하라.
1 <= N <= 1000 / N개 동전 화폐 단위는 1000000 이하의 자연수
"""
n = int(input())
data = list(map(int, input().split()))

data.sort() # 정렬

target = 1 # 만들 수 없는 금액을 1로 초기화
for x in data:
  # 만들 수 없는 금액을 찾으면 반복 종료
  if target < x:
    break
  target += x

print(target)
