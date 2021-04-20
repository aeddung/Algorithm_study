"""
입력값으로 들어오는 N을 반으로 쪼개고 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수 합이 같은지 확인
같다면 'LUCKY'를 출력, 다르다면 'READY'를 출력
"""
# 내가 짠 코드
n = input()

mid = len(n) // 2
sub1 = n[:mid]
sub2 = n[mid:]

result = 0
for i in range(mid):
  diff = int(sub1[i]) - int(sub2[i])
  result += diff

if result == 0:
  print('LUCKY')
else:
  print('READY')
  
#####################################################################################
# 책 예시 코드
n = input()
length = len(n)
summary = 0

# 왼쪽 부분 자릿수 합 더하기
for i in range(length // 2):
  summary += int(n[i])

# 오른쪽 부분 자릿수 합 빼기
for i in range(length // 2, length):
  summary -= int(n[i])
  
if summary == 0:
  print('LUCKY')
else:
  print('READY')
