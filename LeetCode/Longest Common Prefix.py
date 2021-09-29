# vertical scanning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x)) # sort함수 time complexity: O(nlogn)
        
        # strs가 empty인 경우
        if len(strs) == 0:
            return
        else:
            for i in range(len(strs[0])):
                for j in range(1, len(strs)):
                    if strs[0][i] != strs[j][i]: # 달라지는 순간 그때까지의 원소 리턴
                        return strs[0][:i]
            return strs[0]
