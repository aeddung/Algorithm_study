# 파이썬 내장 함수 사용
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        word = s.split(' ')
        return len(word[-1])
      
# 내장 함수 사용하지 않은 버전  
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = len(s) - 1
        while s[idx] == ' ':
            idx -= 1
        
        length = 0
        while idx >= 0 and s[idx] != ' ':
            length += 1
            idx -= 1
        return length
