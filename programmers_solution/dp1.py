"""
문제 설명
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.
12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5
5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.

입출력 예
N                number         return
5                  12              4
2                  11              3

입출력 예 설명
예제 #1
문제에 나온 예와 같습니다.

예제 #2
11 = 22 / 2와 같이 2를 3번만 사용하여 표현할 수 있습니다.
"""

# 참고해서 작성한 코드
def solution(N, number):
  # 인덱스가 N을 몇 번 사용했는지를 나타냄 ex) dp_table[1]: 1번 사용, d_table[4]: 4번 사용
  dp_table = [[]]
  for i in range(1, 9): # N 조건이자 사용 횟수 조건(8보다 크면 -1 리턴)
    case = []
    for j in range(1, i):
        for k in dp_table[j]: # j번 사용한 경우의 수 원소 iteration
          for l in dp_table[i - j]: # i-j번 사용한 경우의 수 원소 iteration
              case.append(k + l) # 더하기
              if k - l >= 0: 
                  case.append(k - l) # 빼기
              case.append(k * l) # 곱하기
              if l != 0 and k != 0:
                  case.append(k // l) # 나누기
    case.append(int(str(N) * i)) # 숫자를 그대로 이어 붙인 케이스 ex) 55, 555
  
    if number in case:
        return i
    dp_table.append(list(set(case)))
  return -1
