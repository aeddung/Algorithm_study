# linear search(runtime: 2224ms)
class Solution:
    def mySqrt(self, x: int) -> int:
        if not 0 < x <= 2**31 - 1:
            return 0
        i = 2
        check = 1
        
        while True:
            if i * i > x:
                return check
            check = i
            i += 1
            
# binary search(runtime: 32ms)
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid <= x and (mid + 1) * (mid + 1) > x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        return low
