from collections import deque

n = int(input())
plan = deque(list(input().split()))

start = (1, 1)

# plan 리스트에 방향 타입이 남아 있는 경우
while plan:
  move = plan.popleft()
  if move == 'R' and start[1] != n: # 오른쪽으로 이동
    next_loc = (start[0], start[1] + 1)
  if move == 'L' and start[1] != 1: # 왼쪽으로 이동
    next_loc = (start[0], start[1] - 1)
  if move == 'U' and start[0] != 1: # 위로 이동
    next_loc = (start[0] - 1, start[1])
  if move == 'D' and start[0] != n: # 아래로 이동
    next_loc = (start[0] + 1, start[1])

  start = next_loc

print(next_loc[0], next_loc[1])
