"""
문제설명: https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3
"""
# 책 예시 코드 참고
def solution(s):
    answer = len(s) # 최악의 경우(반복되는 문자가 하나도 없음)
    
    # 1개 단위부터 압축 단위를 늘려가며 확인(전체 길이의 절반까지)
    for i in range(1, len(s) // 2 + 1):
      compressed = ''
      prev = s[0:i]
      count = 1
      for j in range(i, len(s), i):
          # 단위 크기만큼 증가시키며 이전 문자열과 비교
        if prev == s[j:j+i]:
          count += 1
        else:
          if count >= 2: # 2개 이상 반복될 경우
            compressed += str(count) + prev
          else: # 하나도 반복되지 않을 경우
            compressed += prev
            # 다시 상태 초기화
          prev = s[j:j+i]
          count = 1

      # 남아 있는 문자열 처리
      if count >= 2:
        compressed += str(count) + prev
      else:
        compressed += prev

      answer = min(answer, len(compressed))
  return answer
