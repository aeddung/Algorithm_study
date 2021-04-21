"""
1~N번까지 도시가 존재하고, M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중, 최단 거리가 K인 모든 도시의 번호를 출력하라.
2 <= N <= 300000 / 1 <= M <= 1000000 / 1 <= K <= 300000, 1 <= X <= N
"""
from collections import deque

n, m, k, x = map(int, input().split())

# vertex = [[], [2, 3], [3, 4], []]
# 형식은 인덱스가 현재 노드, 리스트 값이 현재 노드와 연결된 노드들
vertex = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  vertex[a].append(b)

# 거리 초기화
distance = [-1] * m
distance[x] = 0 # 출발 도시까지 거리는 0

q = deque([x])
while q:
  now = q.popleft()
  for next_node in vertex[now]:
    # 아직 방문하지 않은 도시의 경우
    if distance[next_node] == -1:
      # 최단 거리 갱신
      distance[next_node] = distance[now] + 1
      q.append(next_node)

# 최단 거리가 k인 모든 도시의 번호 출력
check = False
for i in range(1, n+1):
  if distance[i] == k:
    print(i)
    check = True

# 최단 거리 k가 없는 경우
if check == False:
  print(-1)
