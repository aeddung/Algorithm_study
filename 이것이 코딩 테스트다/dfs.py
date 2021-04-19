# 섬 최대 개수 구하는 문제와 비슷
"""
N X M 크기의 얼음 틀이 있고, 구멍이 뚫린 부분은 0, 칸막이가 존재하는 부분은 1로 표시
구멍이 뚫린 부분끼리 상, 하, 좌, 우로 붙어 있으면 서로 연결된 것으로 간주
생성되는 총 아이스크림의 개수를 구하기
"""

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x, y):
# 주어진 경로를 벗어나면 종료
  if x < 0 or x >= n or y < 0 or y >= m:
    return False

  # 현재 노드를 아직 방문하지 않았을 경우
  if graph[x][y] == 0:
    graph[x][y] = 1 # 해당 노드 방문 처리
    # 상, 하, 좌, 우 살피기
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    return True
  return False

# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 dfs 실행
    if dfs(i, j) == True:
      result += 1

print(result)
