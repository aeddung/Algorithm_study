class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt_A, cnt_L = 0, 0
        for char in s:
            if char == 'A':
                cnt_A += 1
                cnt_L = 0 # 지각 표시 리셋
            elif char == 'L':
                cnt_L += 1
            else:
                cnt_L = 0 # 지각 표시 리셋
            
            if cnt_A >= 2 or cnt_L >= 3:
                return False
        return True
