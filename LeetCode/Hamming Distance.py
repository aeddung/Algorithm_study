class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        
        distance = 0
        while xor:
            xor &= xor - 1
            distance += 1
        
        return distance
        
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y

        i = xor
        distance = 0
        while i > 0:
            distance += i % 2
            i //= 2
        
        return distance        
