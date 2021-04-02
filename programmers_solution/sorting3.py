"""
문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다.
어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다. 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

입출력 예
citations: [3, 0, 6, 1, 5]
return: 3

입출력 예 설명
이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다.
그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.
"""

# 본인이 짠 코드
def solution(citations):
    answer = 0
    sor_cite = sorted(citations, reverse=True)
    for ele in sor_cite:
        answer += 1
        if ele == answer: # 인용 수와 논문 수가 같을 때가 있을 경우
            return answer
        elif ele < answer: # 인용 수와 논문 수가 다르고, 논문 수보다 작을 때
            return answer - 1
    return answer
  
# 모범 참고 코드 1
def solution(citations):
    citations = sorted(citations) # reverse하지 않음
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
  
# 모범 참고 코드 2
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1))) # 파이썬 내장 함수를 최대한 활용
    return answer
