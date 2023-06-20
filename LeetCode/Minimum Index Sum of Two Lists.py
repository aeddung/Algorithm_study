class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)
        index_sum = {}

        for i, v in enumerate(list1):
            if v in common:
                index_sum[v] = i
        
        for i, v in enumerate(list2):
            if v in common:
                index_sum[v] += i

        min_sum = min(index_sum.values())
        return [v for v, s in index_sum.items() if s == min_sum]
