"""
문제 설명
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

제한사항
문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
"""

def solution(s):    
    dic = {')': '('}
    stack = []
    for char in s:
        if char in dic:
            top_element = stack.pop() if stack else '#'
        
            if dic[char] != top_element:
                return False
        else:
            stack.append(char)
    
    # stack에 '#'가 남아있는 경우(문자열의 첫 원소가 ')'으로 시작하는 예시)
    if stack:
        return False
        
    return True
  
def solution(s):
    cnt = 0
    for char in s:
        if char == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    
    return cnt == 0
