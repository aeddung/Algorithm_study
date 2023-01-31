class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        if n % 2 != 0 or n == 0:
            return False

        while n != 0:
            n = n // 2
            d = n % 2

            if d != 0 and n != 1:
                return False
        
        return True
      
# 모범 코드 1
class Solution:
    def isPowerOfTwo(self, n):
        if n == 0:
          return False
   
        while n % 2 == 0:
            n /= 2
        
        return n == 1  

# 모범 코드 2      
class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and log2(n) == trunc(log2(n))      
