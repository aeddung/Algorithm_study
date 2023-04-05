# runtime 속도 및 memory 공간 우월
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and not(n & (n - 1)) and n & 1431655765 == n
  
# 파이썬 log 함수 및 is_integer() 사용  
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n >= 1 and log(n, 4).is_integer()
