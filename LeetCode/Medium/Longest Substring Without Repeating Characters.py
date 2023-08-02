# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} # 각 원소와 해당 인덱스 조합
        l = 0 # left pointer
        output = 0

        for r in range(len(s)):
            if s[r] not in seen:
                output = max(output, r - l + 1) # 우리가 찾는 length인 동시에 window(left pointer 및 right pointer 구간) size
            else:
                if seen[s[r]] < l: # window 사이에 없을 경우 window size 업데이트
                    output = max(output, r - l + 1)
                else: # window 사이에 존재하는 경우 left pointer 위치 업데이트
                    l = seen[s[r]] + 1
            seen[s[r]] = r # right pointer 업데이트

        return output
