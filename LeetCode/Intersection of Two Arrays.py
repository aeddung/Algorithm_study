# set 자료형 활용
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:        
        intersection_list = set()
        
        compare = set(nums1)
        for i in compare:
            if i in nums2:
                intersection_list.add(i)

        return list(intersection_list)

# 투 포인터 활용
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:        
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0

        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if len(res) == 0 or nums1[i] != res[-1]:
                    res.append(nums1[i])
                i += 1
                j += 1

        return res
 
# 딕셔너리 활용
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:        
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i] + 1 if i in map else 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0
        
        return res
