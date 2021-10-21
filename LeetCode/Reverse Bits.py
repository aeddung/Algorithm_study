class Solution:
    def reverseBits(self, n: int) -> int:
        num = bin(n)[2:]
        
        while len(num) < 32:
            num = '0' + num
        return int(num[::-1], 2)
