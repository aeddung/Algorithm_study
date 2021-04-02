# n은 항상 k보다 크거나 같다
n, k = map(int, input().split())

count = 0

while n != 1:
  if n % k != 0:
    n = n - 1
    count += 1

  else:
    n = n / k
    count += 1

print(count)

###################################

n, k = map(int, input().split())

count = 0

while True:
  target = (n // k) * k
  count += (n - target) # 위처럼 1씩 빼는 것이 아니라 k 배수가 되도록 빼는 과정을 한 번에 처리
  # ex) n이 8이고, k가 2라면 -> 8 - 6 = 2
  n = target
  if n < k:
    break

  count += 1
  n = n / k

# while문 종료된 상태로 n이 k보다 작다. n이 1이 되도록 하는 값을 count 해준다.
count += (n - 1)
print(count)
