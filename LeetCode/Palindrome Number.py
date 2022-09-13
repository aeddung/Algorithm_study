class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # 음수의 경우 모두 False
            return False
        
        x = str(x)
        
        for i in range(len(x) // 2):
            if x[i] != x[len(x) - 1 - i]:
                return False
        
        return True
      
# 인기 많은 Python solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]
