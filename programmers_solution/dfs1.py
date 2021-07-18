# 첫 번째 방법(재귀구조 DFS)
answer = 0
# DFS 이용
def dfs(idx, result, numbers, target):
    global answer
    if idx == len(numbers): # numbers 원소를 모두 계산했을 경우
        if result == target:
            answer += 1
        return
    else:
        dfs(idx + 1, result + numbers[idx], numbers, target) # 재귀구조
        dfs(idx + 1, result - numbers[idx], numbers, target)

def solution(numbers, target):
    global answer # 전역 변수 사용
    dfs(0, 0, numbers, target) # result = 0으로 초기화
    
    return answer
  
#####################################################################################
# 두 번째 방법(stack DFS)
def solution(numbers, target):
    answer = 0
    stack = [[numbers[0], 0], [-1 * numbers[0], 0]] # [계산값, 인덱스]
    while stack:
        tmp, idx = stack.pop()
        idx += 1
        if idx < len(numbers):
            stack.append([tmp + numbers[idx], idx])
            stack.append([tmp - numbers[idx], idx])
        else: # numbers의 모든 원소를 다 계산했을 경우 -> 이때 stack은 empty 상태
            if tmp == target:
                answer += 1
    return answer
  
#####################################################################################
# 세 번째 방법(queue BFS)
from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque([[numbers[0], 0], [-1 * numbers[0], 0]])
    while queue:
        tmp, idx = queue.popleft()
        idx += 1
        if idx < len(numbers):
            queue.append([tmp + numbers[idx], idx])
            queue.append([tmp - numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
    return answer
