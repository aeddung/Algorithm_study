# nested for 문을 꼭 3개 써야 할까 고민하며 이것저것 시도... 
n = int(input())

count = 0
# 60 x 60 x 24

min_sec = []

for i in range(60): # 분
  for j in range(60): # 초
    min_sec.append([i, j])

for c in range(n + 1):
  grouped = list(map(lambda x: [c] + x, min_sec)) # grouped format: [시간, 분, 초]
  for _ in grouped:
    if '3' in str(_[0]) + str(_[1]) + str(_[2]): # 시간, 분, 초를 string으로 변환한 뒤 합침
      count += 1
      
print(count)

############################################################################################

# 답안 예시 -> 3중 for문
n = int(input())

count = 0
for i in range(n + 1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1
        
print(count)
