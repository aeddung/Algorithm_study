class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:] # bin() 결과에서 앞에 나오는 0b 제외
        flipped = ''.join(['0' if bit == '1' else '1' for bit in binary])
        
        if flipped:
            return int(flipped, 2) # int(value, base): base는 진수를 의미
            
class Solution:
    def findComplement(self, num: int) -> int:
        num ^ (2 ** (len(bin(num)[2:])) - 1)
