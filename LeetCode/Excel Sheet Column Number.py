# runtime: 70ms
import string
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0
        i = len(columnTitle) - 1
        dic = {letter: n for letter, n in zip(string.ascii_uppercase, range(1, 26 + 1))}
        for char in columnTitle:
            answer += dic[char] * 26**i
            i -= 1
            
        return answer

# runtime: 49ms      
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        value = 0
        counter = 0
        
        for column_char in columnTitle[::-1]: # 뒤에서부터 훑기
            add_value = ord(column_char) - 64
            add_value *=  26 ** counter
                
            value += add_value
            counter += 1
        
        return value      
