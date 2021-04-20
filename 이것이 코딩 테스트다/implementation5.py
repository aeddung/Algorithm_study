"""
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어짐
모든 알파벳을 오름차순으로 정렬하고 이어서 모든 숫자를 더한 형태를 출력
"""
# 본인이 작성한 코드
s = input()

alpha = []
num = []
for i in s:
  if i.isalpha():
    alpha.append(i)
  else:
    num.append(i)

alpha.sort()
summary = 0
for i in num:
  summary += int(i)

alpha = ''.join(alpha) + str(summary)
print(alpha)

##########################################################################################
# 책 예시 코드 <- 숫자 0만 올 경우 출력값에서 생략되는 문제 발생
data = input()
result = []
value = 0

# 문자를 하나씩 확인
for x in data:
  if x.isalpha():
    result.append(x)
  else:
    value += int(x)
    
result.sort()
# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입 <- 문제가 되는 코드 구간(입력값에 0이 오면 출력값에도 0이 있어야 한다)
if value != 0:
  result.append(str(value))
  
# 리스트를 문자열로 변환하여 출력
print(''.join(result))
