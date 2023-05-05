class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n >= i:
            n -= i
            i += 1

        return i - 1

# binary search
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            coins = (mid * (mid + 1)) // 2 # mid 층까지 모든 코인이 채워졌을 때의 코인 갯수

            if coins <= n: # 가지고 있는 코인이 더 남는 경우
                left = mid + 1
            else: # 코인이 모자른 경우
                right = mid - 1
            
        return right    
