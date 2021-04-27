"""
N개의 수로 이루어진 수열 A1, A2, ..., An이 있다. 또, 수와 수 사이에 끼워 넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈, 뺄셈, 곱셈, 나눗셈으로만 이루어져 있다.
수와 수 사이에 연산자를 하나씩 넣어 수식을 하나 만들 수 있는데, 주어진 수열의 순서는 바꿀 수 없다.
식의 계산은 연산자 우선순위를 무시한 채 앞에서부터 진행하며 나눗셈은 정수 나눗셈으로 몫만 취한다.
만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성해라.
2 <= N <= 11 / 1 <= Ai <= 100
"""

n = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split()) # 순서 +, -, x, /

# 최솟값과 최댓값 초기화
min_val = 1e9
max_val = -1e9

# i: 숫자 사용 수 / now: 연산자를 통해 계산된 현재 값
def dfs(i, now): 
  global min_val, max_val, add, sub, mul, div
  # 모든 연산자를 다 사용한 경우
  if i == n:
    min_val = min(min_val, now)
    max_val = max(max_val, now)

  else:
    # 각 연산자에 대해 재귀 반복
    if add > 0:
      add -= 1
      dfs(i + 1, now + num_list[i])
      add += 1 # 바로 위의 dfs가 끝났기 때문에 global 변수인 add는 원래 값으로 변경 -> 다음 연산자 작업 때 영향을 주지 않기 위함
    if sub > 0:
      sub -= 1
      dfs(i + 1, now - num_list[i])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(i + 1, now * num_list[i]) 
      mul += 1
    if div > 0:
      div -= 1
      dfs(i + 1, now / num_list[i])
      div += 1

dfs(1, num_list[0])
print(max_val)
print(min_val)
