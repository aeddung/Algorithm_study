# runtime: 44ms
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        if len(s) < k:
            return s[::-1]

        interval = 2 * k
        for i in range(0, len(s), interval):
            if i == 0:
                ans += s[i + k - 1::-1]
                ans += s[i + k:i + interval]
            else:
                ans += s[i + k - 1:i - 1:-1]
                ans += s[i + k: i + interval]
                
        return ans
      
# runtime: 47ms      
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]
        return s[:k][::-1] + s[k:2 * k] + self.reverseStr(s[2 * k:], k)      
