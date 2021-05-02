"""
각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 확인하며 'x', '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하라.
단, 일반적인 계산 방식과 달리 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정한다. 
1 <= S <= 20
"""
# 내가 짠 코드 <- 숫자가 0과 1이라면 더하는 것이 무조건 크다는 사실을 간과, +한 결과값이랑 x한 결과값이랑 매번 비교함...
s = input()

for i in range(len(s) - 1):
  if i == 0:
    re1 = int(s[i]) + int(s[i + 1])
    re2 = int(s[i]) * int(s[i + 1])
  else:
    re1 = result + int(s[i + 1])
    re2 = result * int(s[i + 1])
  result = max(re1, re2)

print(result)

###################################################

data = input()
result = int(data[0])

for i in range(1, len(data)):
  num = int(data[i])
  if num <= 1 or result <= 1: # 숫자과 0과 1이라면 +, 아니라면 x
    result += num
  else:
    result *= num
   
print(result)
