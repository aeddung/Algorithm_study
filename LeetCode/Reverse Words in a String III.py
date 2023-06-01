class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        words = s.split(' ')
        for word in words:
            ans += word[::-1] + ' '

        return ans[:-1]
