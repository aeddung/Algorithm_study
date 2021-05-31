"""
문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.

입출력 예
number               k                  return
"1924"               2                   "94"
"1231234"            3                  "3234"
"4177252841"         4                 "775841"
"""
# 참고하여 작성한 코드
def solution(number, k):
    stack = [number[0]]
    for i in number[1:]:
        while len(stack) > 0 and stack[-1] < i and k > 0:
            k -= 1 # 지워야 하는 숫자 개수 count
            stack.pop() # 새로 들어오는 값보다 작으면 삭제
        stack.append(i)
        
    if k != 0: # 같은 숫자가 연속으로 나올 경우
        stack = stack[:-k] # 위에서 pop()이 작동하지 않기 때문에 끊어줘야 함
    return ''.join(stack)
