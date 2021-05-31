# 재귀 반복 구조
def binary_search(array, target, start, end):
  if start > end: # base case
    return
  mid = (start + end) // 2
  # 찾은 경우 인덱스 반환
  if array[mid] == target:
    return mid
  elif array[mid] > target: # 중간값이 목표값보다 큰 경우 중간값 왼쪽에서 찾기
    return binary_search(array, target, start, mid - 1)
  else: # 중간값이 목표값보다 작은 경우 중간값 오른쪽에서 찾기
    return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

# binary search result
result = binary_search(array, target, 0, n - 1)
if result == None:
  print('원소가 존재하지 않음')
else:
  print(result + 1) # 인덱스가 아닌 몇 번째 있는지 출력
  
# 일반 반복문
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
  print('원소가 존재하지 않음')
else:
  print(result + 1)
