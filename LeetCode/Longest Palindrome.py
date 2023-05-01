class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        odd_count = 0
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
            
            if dic[char] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1
        
        if odd_count > 1:
            return len(s) - odd_count + 1
        
        return len(s)
      
class Solution:
    def longestPalindrome(self, s: str) -> int:
        unpairedLetter = set()
        palindromeLength = 0

        for char in s:
            if char in unpairedLetter:
                palindromeLength += 2
                unpairedLetter.remove(char)
            else:
                unpairedLetter.add(char)
        
        if len(unpairedLetter) > 0:
            return palindromeLength + 1
        
        return palindromeLength
