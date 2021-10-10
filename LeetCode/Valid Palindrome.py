from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        stack = []
        for char in s:
            if char.isalnum(): # 알파벳 혹은 숫자인지 확인
                stack.append(char)
       
        queue = deque(stack)
        while len(stack) > 1:
            if stack.pop() != queue.popleft():
                return False
        
        return True
