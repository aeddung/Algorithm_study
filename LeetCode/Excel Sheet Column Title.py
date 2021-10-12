# runtime: 44ms
class Solution:
    def convertToTitle(self, columnNumber):
        answer = ''
        while columnNumber != 0:
            tmp = chr(ord('A') + (columnNumber - 1) % 26)
            columnNumber = (columnNumber - 1) // 26
            answer = tmp + answer
        return answer
      
# runtime: 42ms      
from collections import deque
import string
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dic = {n: letter for n, letter in zip(range(26), string.ascii_uppercase)} # string.ascii_uppercase: AB...Z 출력
        queue = deque()
        while columnNumber > 0:
            num = (columnNumber - 1) % 26
            queue.appendleft(dic[num])
            columnNumber = (columnNumber - 1) // 26
            
        return ''.join(queue)
