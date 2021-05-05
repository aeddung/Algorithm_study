"""
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

입출력 예
numbers             return
"17"                   3
"011"                  2

입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
- 11과 011은 같은 숫자로 취급합니다.
"""
from itertools import permutations
import math

# 소수 판별 함수
def check(n): 
    k = math.sqrt(n) # 제곱근까지만 봐도 소수 판별 가능
    if n < 2: # 1은 소수가 아님
        return False

    for i in range(2, int(k) + 1): # 16을 예로 들면, (2, 8), (4, 4), (8, 2), 즉 (8, 2)까지 가지 않고 4까지만 보면 됨
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for n in range(1, len(numbers) + 1): # 각 원소 개수로 만들 수 있는 모든 경우의 수
        per = list(map(''.join, permutations(list(numbers), n))) # n개 원소 조합으로 수열 만들기
        for i in list(set(per)): # 반복 숫자 set으로 제거
            if check(int(i)):
                answer.append(int(i))

    answer = len(set(answer)) # 각 원소 개수로 만든 숫자에서 발생할 수 있는 반복 제거
    return answer
