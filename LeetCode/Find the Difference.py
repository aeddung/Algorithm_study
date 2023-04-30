class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for letter in s:
            if letter not in dic:
                dic[letter] = 1
            else:
                dic[letter] += 1
        
        for letter in t:
            if letter not in dic or dic[letter] == 0:
                return letter
        
            else:
                dic[letter] -= 1
              
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for letter in s:
            res ^= ord(letter) # ord: 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수 반환 / 비트연산자 ^: 이진수 기준 XOR
        for letter in t:
            res ^= ord(letter)
        return chr(res) # chr: 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자 반환
