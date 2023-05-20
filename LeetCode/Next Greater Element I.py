class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        dic = {}
        stack = [nums2[0]]

        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                dic[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])

        for element in stack:
            dic[element] = -1
        
        for i in range(len(nums1)):
            answer.append(dic[nums1[i]])
        return answer
