class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = ''
        # 자릿수 맞추기
        if len(a) != len(b):
            if len(a) > len(b):
                for _ in range(len(a) - len(b)):
                    b = '0' + b
            else:
                for _ in range(len(b) - len(a)):
                    a = '0' + a
                    
        std_len = max(len(a), len(b))
        
        if a[-1] == '1' and b[-1] == '1':
            carry = True
            answer = '0' + answer
        else:
            carry = False
            if a[-1] == '0' and b[-1] == '0':
                answer = '0' + answer
            else: # 둘 중 하나만 1인 경우
                answer = '1' + answer
        
        for i in range(std_len - 2, -1, -1): # 뒤에서 2번째 원소부터 진행
            if a[i] == '1' or b[i] == '1':
                if a[i] == '1' and b[i] == '1':
                    if carry == True:
                        answer = '1' + answer
                    else:
                        answer = '0' + answer
                    carry = True # 항상 True가 되어야 함
                else: # 둘 중 하나만 1일 경우
                    if carry == True:
                        answer = '0' + answer
                    else:
                        answer = '1' + answer
                        
            else: # 둘 다 0일 경우
                if carry == True:
                    answer = '1' + answer
                else:
                    answer = '0' + answer
                carry = False # 항상 False가 되어야 함
        
        # 자릿수 넘어가는 경우 확인
        if carry == True:
            answer = '1' + answer
        
        return answer
