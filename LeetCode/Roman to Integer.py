class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        result = 0
        dic = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        
        for i in dic:
            if i in s:
                result += dic[i]
                s = s.replace(i, '')
                
        for j in s:
            result += symbol[j]
            
        return result
