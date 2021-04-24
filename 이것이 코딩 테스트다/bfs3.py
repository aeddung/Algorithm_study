"""
N x N 크기의 시험관이 있으며 1 x 1 크기의 칸으로 나뉜다. 특정한 위치에 바이러스가 존재하며, 바이러스 종류는 1~K 번까지 K개가 있다.
바이러스는 1초마다 상, 하, 좌, 우 방향으로 증식하는데, 매초 번호가 낮은 종류의 바이러스부터 먼저 증식한다.
증식 과정에서 특정 칸에 이미 어떤 바이러스가 있다면, 그곳에는 다른 바이러스가 들어갈 수 없다.
s초가 지난 후 (X, Y)에 존재하는 바이러스 종류를 출력하는 프로그램을 작성하라. 바이러스가 없다면 0을 출력해라.
시험관의 가장 왼쪽 위에 해당하는 곳은 (1, 1)에 해당한다. 
1 <= N <= 200 / 1 <= K <= 1000 / 0 <= S <= 10000 / 1 <= X, Y <= N
"""
from collections import deque

n, k = map(int, input().split())
array = [] # 시험관 그래프
data = [] # 바이러스 정보 기입할 리스트
for i in range(n):
  array.append(list(map(int, input().split())))
  for j in range(n):
    if array[i][j] != 0:
      # (바이러스 종류, 시간, x좌표, y좌표) 삽입
      data.append((array[i][j], 0, i, j))

# 바이러스 종류는 번호가 낮은 것부터 증식하므로 정렬
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while q:
  virus, s, x, y = q.popleft()
  # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
  if s == target_s:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < n and ny >= 0 and ny < n:
      if array[nx][ny] == 0:
        array[nx][ny] = virus
        q.append((virus, s + 1, nx, ny))

print(array[target_x - 1][target_y - 1]) # 좌표가 (0, 0)부터 시작하는 것이 아니라 (1, 1)부터 시작
