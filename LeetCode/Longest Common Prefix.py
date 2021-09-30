# vertical scanning(runtime: 36ms)
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

# binary search(runtime: 36ms)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return
        else:
            target = strs[0]
            
            remains = strs[1:]
            if not remains: # strs에 1개 원소밖에 없을 때
                return target
            left = 0
            right = len(target) - 1
            
            mid = ((left + right) // 2)
            while left <= right:
                if self.isCommonPrefix(target[:mid + 1], remains):
                    left = mid + 1
                else:
                    right = mid - 1
                mid = ((left + right) // 2)
        return target[:mid + 1]
                
                
    def isCommonPrefix(self, target, remains):
        for x in remains:
            if not x.startswith(target): # 남은 원소들의 시작하는 글자 확인
                return False
        return True

# divde and conquer(runtime: 52ms)
class Solution:
    def commonPrefix(self, str1, str2):
        result = ''
        n1, n2 = len(str1), len(str2)
        i, j = 0, 0
        
        while i <= n1 - 1 and j <= n2 - 1:
            if str1[i] != str2[j]:
                break
            result += str1[i]
            i, j = i + 1, j + 1
        return result
    
    def longestCommonPrefixHelp(self, strs: List[str], low: int, high: int) -> str:
        if low == high:
            return strs[low]
        
        if high > low:
            mid = low + (high - low) // 2
            
            str1 = self.longestCommonPrefixHelp(strs, low, mid)
            str2 = self.longestCommonPrefixHelp(strs, mid + 1, high)
            
            return self.commonPrefix(str1, str2)
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return
        return self.longestCommonPrefixHelp(strs, 0, len(strs) - 1)
