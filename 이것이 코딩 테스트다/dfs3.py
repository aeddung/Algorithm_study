"""
해당 문제는 카카오 2020 신입 공채 1차 문제다. 문제 설명은 아래 프로그래머스 사이트에서 참고하길 바란다.
https://programmers.co.kr/learn/courses/30/lessons/60058
"""

# 균형잡힌 괄호 문자열 index 반환
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0: # 균형 잡혔다고 판단되는 해당 위치의 index
            return i

# 올바른 괄호 문자열인지 판단
def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # '('가 등장하지 않거나 ')'가 연속해서 등장한 경우
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1] # 균형잡힌 index 이전까지
    v = p[index + 1:] # 위 index 이후
    
    # 1) u가 올바른 괄호 문자열인 경우
    if check_proper(u):
        answer = u + solution(v) # 재귀
    
    # 2) u가 올바른 괄호 문자열이 아닌 경우 문제에서 제시한 step을 그대로 수행
    else:
        answer = '('
        answer += solution(v) # 재귀
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)

    return answer
