# runtime: 362ms
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        history = []
        for n in nums:
            if n == 1:
                max_length += 1
            else:
                history.append(max_length)
                max_length = 0

            if n == nums[-1]: # 마지막 원소가 1일 경우
                history.append(max_length)
        
        return max(history)
        
# runtime: 333ms        
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0) # 마지막 원소가 1일 경우 대비
        ans, max_length = 0, 0
        for n in nums:
            if n:
                max_length += 1
            else:
                ans = max(max_length, ans)
                max_length = 0
        
        return ans
