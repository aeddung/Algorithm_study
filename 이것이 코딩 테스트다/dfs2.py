"""
N x M 크기의 연구소가 존재하며, 이는 1 x 1 크기의 정사각형으로 나누어져 있다.
연구소는 빈칸, 벽으로 이루어져 있으며, 일부 칸은 바이러스가 존재한다. 이 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있다.
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
0은 빈칸, 1은 벽, 2는 바이러스를 가리킨다. 바이러스가 퍼질 수 없는 곳을 안전 영역(즉 0)이라고 하며, 최댓값을 구하는 프로그램을 작성해라.
3 <= N, M <= 8 / 2 <= 바이러스 개수 <= 10 / 3 <= 빈칸 개수
"""
n, m = map(int, input().split())
array = [] # 초기 맵 리스트

# 모든 자리에 벽을 설치한 리스트(초기화)
temp = [[0] * m for _ in range(n)] 

for _ in range(n):
    array.append(list(map(int, input().split())))

# 순서대로 하, 우, 상, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
# dfs로 바이러스가 사방에 퍼지도록
def virus(x, y):
  for i in range(4):
    # 상, 하, 좌, 우를 살피기
    nx = x + dx[i]
    ny = y + dy[i]
    # 연구소 내에 있을 경우만
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      if temp[nx][ny] == 0:
        # 바이러스 뿌리기
        temp[nx][ny] = 2
        virus(nx, ny) # 그 자리에서 다시 반복 수행

# 현재 맵에서 안전영역 크기 계산
def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score

# dfs를 통해 울타리 설치 및 매번 안전영역 크기 계산
def dfs(count):
  global result
  # 울타리가 3개 설치된 경우 안전영역 계산
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = array[i][j]

    # 각 바이러스 위치에서 전파 수행
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i, j)

    result = max(result, get_score())
    return

  # 빈 공간에 울타리 설치
  for i in range(n):
    for j in range(m):
      if array[i][j] == 0:
        array[i][j] = 1
        count += 1
        dfs(count) # count = 3일 경우, result에 안전영역을 저장하고 종료
        array[i][j] = 0 # 쌓아왔던 3개의 벽 다시 제거
        count -= 1

dfs(0)
print(result)
