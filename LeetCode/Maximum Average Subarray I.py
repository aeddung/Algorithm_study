class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])

        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k] # 오른쪽으로 하나씩 이동하며 업데이트
            maxSum = max(maxSum, currSum)

        return maxSum / k
