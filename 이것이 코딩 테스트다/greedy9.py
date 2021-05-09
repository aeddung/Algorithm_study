"""
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
