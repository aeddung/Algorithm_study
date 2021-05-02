"""
한 마을에 모험가 N명이 있다. N명 모두 공포도를 측정했는데, 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 그룹에 참여해야 여행을 떠날 수 있다.
N명의 모험가에 대한 정보가 주어질 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하라.
1 <= N <= 100,000 / 공포도는 N이하의 자연수로 주어진다.
"""
# 내가 짠 코드 <- 그리디를 복잡하게 구현할 필요가 없다. 꼭 리스트를 만들어 문제 설명처럼 그룹을 만들 필요 없이 변수로도 충분히 나타낼 수 있다는 점을 기억하자.
n = int(input())
degree = list(map(int, input().split()))

degree.sort()

group = []
for i in range(len(degree)):
  if degree[i] == 1: # 공포도 1이면 계속 혼자 그룹 생성
    group.append([degree[i]])
  else:
    if i + degree[i] >= len(degree): # 전체 모험가 숫자를 넘어가게 되면 어차피 그룹이 형성되지 않음
      break
    else:
      if degree[i] >= degree[i + degree[i]]: # 처음 선택한 모험가의 공포도가 끝에 있는 모험가보다 클 경우
        group.append([degree[i:i + degree[i]]])
      
print(len(group))

#################################################

n = int(input())
data = list(map(int, input().split())
data.sort()
            
result = 0 # 그룹 수
count = 0 # 현재 그룹에 포함된 모험가 수
for i in data:
  count += 1 # 현재 그룹에 해당 모험가 포함
  if count >= i: # 현재 그룹에 포함된 모험가 수가 현재 공포도 이상이라면 그룹 결성
    result += 1 # 그룹 수 증가
    count = 0 # 현재 그룹에 포함된 모험가 수 초기화
            
print(result)
