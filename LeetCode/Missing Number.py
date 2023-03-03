class Solution:
    def missingNumber(self, nums: List[int]) -> int: 
        max_num = len(nums)
        return list((set([i for i in range(max_num + 1)]).difference(set(nums))))[0]
      
# 참고 코드      
class Solution:
    def missingNumber(self, nums: List[int]) -> int: 
        currSum = sum(nums)
        corrSum = len(nums) * (len(nums) + 1) // 2
        return corrSum - currSum
