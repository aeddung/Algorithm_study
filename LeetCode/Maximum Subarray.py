# 첫 번째 방법
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0: # 이전의 숫자가 양수일 때만 더하기
                nums[i] += nums[i - 1]
        
        return max(nums)
      
# 두 번째 방법
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums
        for i in range(1, len(nums)):
            result[i] = max(result[i - 1] + nums[i], nums[i])
        
        return max(result)
