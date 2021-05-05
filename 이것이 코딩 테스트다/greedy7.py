"""
0과 1로만 이루어진 문자열 S가 있다. S의 모든 숫자를 전부 같게 만드려고 한다. 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다. S를 모두 같은 숫자로 바꾸기 위해 숫자를 뒤집는 최소 횟수를 출력하라.
S의 길이는 100만보다 작다.
"""

# 모두 0으로 바꾸거나, 1로 바꾸거나 하는 경우를 생각하지 않은 채 작성한 코드 <- 오류 발생 가능성 높음
s = input()
init_val = s[0]
count = 0

for i in s[1:]:
  val = i
  if init_val != val:
    count += 1
  init_val = val

print(int(count / 2))

############################################################

data = input()
count0 = 0 # 전부 0으로 바꾸는 경우 -> 1을 발견하면 count0 +=1 
count1 = 0 # 전부 1로 바꾸는 경우 -> 0을 발견하면 count1 += 1

if data[0] == '1':
  count0 += 1
else:
  count1 += 1

for i in range(len(data)- 1):
  if data[i] != data[i + 1]:
    # 다음 수에서 1로 바뀌는 경우
    if data[i + 1] == '1':
      count0 += 1
    # 다음 수에서 0으로 바뀌는 경우
    else:
      count1 += 1

print(min(count0, count1))
