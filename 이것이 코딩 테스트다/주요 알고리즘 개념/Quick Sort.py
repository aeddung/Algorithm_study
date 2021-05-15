array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start: int, end: int) -> None:
  if start >= end: # 원소가 1개인 경우 base case
    return
    
  pivot = start # 첫 번째 원소를 pivot으로(호어 분할 방식)
  left = start + 1
  right = end
  while left <= right:
    # pivot보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1
    # pivot보다 작은 데이터를 찾을 때까지 반복
    while right > start and array[right] >= array[pivot]:
      right -= 1
    
    if left > right: # 엇갈렸다면 작은 데이터와 피봇 교체
      array[right], array[pivot] = array[pivot], array[right]
    else: # 엇갈리지 않았다면 왼쪽(큰값)과 오른쪽(작은값) 교체
      array[left], array[right] = array[right], array[left]

  # 분할 이후 왼쪽, 오른쪽 부분에서 각자 정렬 수행
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
