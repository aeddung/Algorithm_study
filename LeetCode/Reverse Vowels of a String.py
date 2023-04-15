class Solution:
    def reverseVowels(self, s: str) -> str:
        loc = []
        s = list(s)

        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                loc.append(i)

        for i in range(len(loc) // 2):
            s[loc[i]], s[loc[-i-1]] = s[loc[-i-1]], s[loc[i]]

        return ''.join(s)
      
# 튜플 활용      
class Solution:
    def reverseVowels(self, s: str) -> str:
        answer = ''
        master_list = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

        vowel_list = ''
        for i in range(1, len(s) + 1):
            if s[-i] in master_list:
                vowel_list += s[-i]

        vowel_count = 0
        for j in range(len(s)):
            if s[j] in vowel_list:
                answer += vowel_list[vowel_count]
                vowel_count += 1
            else:
                answer += s[j]

        return answer  
