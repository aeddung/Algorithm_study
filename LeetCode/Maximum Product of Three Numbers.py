class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        result1 = nums[-1] * nums[-2] * nums[-3]
        result2 = nums[-1] * nums[0] * nums[1]
        return max(result1, result2)
