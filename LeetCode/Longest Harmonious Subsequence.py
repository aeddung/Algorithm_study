class Solution:
    def findLHS(self, nums: List[int]) -> int:
        mapping = {}
        max_length = 0
        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1
        
        for key in mapping:
            if key + 1 in mapping:
                max_length = max(max_length, mapping[key] + mapping[key + 1])
            
        return max_length
