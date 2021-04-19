"""
N X M 크기의 직사각형 미로에 괴물이 있는 부분은 0으로, 없는 부분은 1로 표시되어 있음
현재 위치는 좌표로 보자면 (0, 0)이고 미로의 시작 칸과 마지막 칸은 항상 1
탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하기(미로는 반드시 탈출할 수 있는 형태로 제시됨)
"""

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))
  
# 순서대로 서, 동, 남, 북
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
  q = deque()
  q.append((x, y)) # 현재 노드 방문 처리

  # 큐가 빌 때까지 반복
  while q:
    x, y = q.popleft()
    # 현재 위치에서 동서남북 방향 살피기
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 미로를 벗어난 경우 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      # 괴물이 있을 경우 무시
      if graph[nx][ny] == 0:
        continue
      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))
  return graph[n-1][m-1] # 맨 오른쪽 아래 노드에 최단 거리가 기록되어 있음

print(bfs(0, 0))
