"""
전자 매장에 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 견적서를 요청했다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
부품의 고유한 번호는 1보다 크고 1,000,000 이하이다.
1 <= N <= 1,000,000 / 1 <= M <= 100,000
"""
# 반복문으로 구현한 binary search
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

n = int(input())
array = list(map(int, input().split()))
array.sort() # requiremnt of binary search
m = int(input())
x = list(map(int, input().split()))

# 손님이 찾고자 하는 부품 번호
for i in x:
  result = binary_search(array, i, 0, n - 1)
  if result == None:
    print('no', end=' ')
  else:
    print('yes', end=' ')
