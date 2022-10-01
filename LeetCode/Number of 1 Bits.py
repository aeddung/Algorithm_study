class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        result = n.count('1')
        
        return result
