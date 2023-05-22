class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        answer = ''
        flat = 0

        # 음수일 경우
        if num < 0: 
            num = -num
            flat = 1

        while num != 0:
            r = num % 7
            answer = str(r) + answer
            num //= 7

        if flat:
            return '-' + answer
        return answer
