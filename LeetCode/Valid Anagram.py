class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        for idx, char in enumerate(s):
            if s[idx] != t[idx]:
                return False

        return True
      
#       
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = {}

        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        
        for char in t:
            if char not in dic or dic[char] == 0:
                return False
            else:
                dic[char] -= 1

        return True
