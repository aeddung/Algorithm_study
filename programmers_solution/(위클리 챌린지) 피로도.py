def enter(dungeons, k, i):
  global answer
  k -= dungeons[i][1]
  answer = max(answer, sum(visited))
  
  for j in range(len(dungeons)):
    if not visited and  k >= dungeons[j][0]:
      visited[j] = 1
      enter(dungeons, k, j)
      visited[j] = 0

def solution(k, dungeons):
  global visited
  visited = [0] * len(dungeons)
  for i in range(len(dungeons)):
    if k >= dungeons[i][0]:
      visited[i] = 1
      enter(dungeons, k, i)
      visited[i] = 0
  return answer
