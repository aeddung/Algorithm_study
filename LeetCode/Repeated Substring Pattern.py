# runtime: 70ms
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if s[:i] * (n // i) == s:
                    return True

        return False

# runtime: 152ms
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1):
            if s == s[i:] + s[:i]:
                return True
        return False
