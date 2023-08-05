# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res, curSum, l = len(nums) + 1, 0, 0
        for r, n in enumerate(nums):
            curSum += n
            while curSum >= target and l <= r:
                res = min(res, r - l + 1)
                curSum -= nums[l]
                l += 1
        return res % (len(nums) + 1) # nums 원소들을 다 더해도 target보다 작을 경우 0 리턴
