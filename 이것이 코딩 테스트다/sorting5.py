"""
두 개의 배열 A와 B가 있다. 두 배열은 N개의 원소로 구성되어 있으며, 모두 자연수이다.
최대 K번의 바꿔치기 연산을 수행할 수 있는데, 이때 바꿔치기란 A에 있는 원소와 B에 있는 원소를 서로 바꾸는 것을 의미한다.
K번의 바꿔치기를 하여 만들 수 있는 A의 모든 원소 합의 최댓값을 출력하는 프로그램을 작성해라.
1 <= N <= 100,000 / 0 <= K <= N / 모든 원소는 10,000,000보다 작은 자연수
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else: # 더 이상 반복문을 돌 필요 없음 -> 효율성
    break

print(sum(a))
