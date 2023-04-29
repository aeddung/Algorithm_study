class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for v in ransomNote:
            if v not in dic:
                dic[v] = 1
            else:
                dic[v] += 1

        for j in magazine:
            if j in dic and dic[j] != 0:
                dic[j] -= 1

        if sum(dic.values()) == 0:
            return True
        return False
        
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char not in magazine:
                return False
            else:
                magazine = magazine.replace(char, '', 1) # replace(oldvalue, newvalue, count): count는 oldvalue를 발견할 때마다 몇 개 바꿀 것인지, 디폴트는 모든 oldvalue
        return True
