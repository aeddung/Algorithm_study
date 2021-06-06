from typing import List
def mergeSortHelp(L: List, first: int, last: int) -> None:
  # 리스트 반으로 쪼개기
  if first == last:
    return
  else:
    mid = first + (last - first) // 2 # integer overflow 방지(파이썬은 상관 무)
    mergeSortHelp(L, first, mid)
    mergeSortHelp(L, mid + 1, last)
    # 다 쪼개고 난 뒤에 merge 함수 호출
    merge(L, first, mid, last)

def merge(L: List, first: int, mid: int, last: int) -> None:
  # 쪼갠 리스트를 다시 합치기
  sub1 = L[first:mid + 1]
  sub2 = L[mid + 1:last + 1]
  i = j = 0 # sublist1, sublist2의 각 인덱스
  k = first # 정렬 리스트 인덱스

  while i < len(sub1) and j < len(sub2):
    if sub1[i] <= sub2[j]:
      L[k] = sub1[i]
      i += 1
    else:
      L[k] = sub2[j]
      j += 1
    k += 1

  if i < len(sub1):
    L[k:last + 1] = sub1[i:]
  elif j < len(sub2):
    L[k:last + 1] = sub2[j:]

# 삽입 정렬 함수 호출
def mergeSort(L: List) -> None:
  mergeSortHelp(L, 0, len(L) - 1)

array = [5, 3, 2, 6, 9, 7, 1, 4]
mergeSort(array)
print(array)
