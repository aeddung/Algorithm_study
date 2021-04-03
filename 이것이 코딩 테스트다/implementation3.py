r, c = input().split()

c_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
c = c_list.index(c)
r = int(r)

count = 0

# 나이트가 이동할 수 있는 경로 모음
condition = [(r - 1, c - 2), (r + 1, c + 2), (r - 1, c + 2), (r + 1, c - 2),
(r + 2, c - 1), (r - 2, c - 1), (r + 2, c + 1), (r - 2, c + 1)]

for nex_loc in condition:
  if 0 < nex_loc[0] < 9 and -1 < nex_loc[1] < 8:
    count += 1

print(count)

##################################################################################

# 입력받는 부분에서 아스키로 처리 가능
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 입력한 문자의 아스키 코드와 column 첫 번째 값인 a 아스키 코드를 비교해서 위치를 숫자로 변환
