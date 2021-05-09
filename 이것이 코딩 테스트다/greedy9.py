"""
A, B 두 사람이 볼링을 치고 있으며 서로 무게가 다른 볼링공을 고르려고 한다.
볼링공은 총 N개가 있고, 무게가 적혀 있으며, 번호는 1번부터 순서대로 부여된다.
같은 무게의 공이 있을 수 있지만, 서로 다른 공으로 간주한다.
볼링공 무게는 1부터 M까지 자연수 형태로 존재한다. 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하라.
1 <= N <= 1000, 1 <= M <= 10, 1 <= K(볼링공 무게) <= M
"""
# 내가 작성한 코드
n, m = map(int, input().split())
data = list(map(int, input().split()))

result = []
for i in range(len(data)):
  for j in range(i, len(data)):
    if data[i] != data[j]:
      if (i, j) not in result:
        result.append((i, j))

print(len(result))

###########################################################################

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지 무게를 담을 수 있는 리스트
array = [0] * 11
for x in data:
  array[x] += 1 # 무게에 해당하는 볼링공 개수 카운트
  
result = 0
for i in range(1, m + 1):
  n -= array[i] # 무게가 i인 볼링공 개수(A가 선택할 수 있는 개수) 제외
  result += array[i] * n # B가 선택할 수 있는 개수(=n)와 곱하기
  
print(result)
