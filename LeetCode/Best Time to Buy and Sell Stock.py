class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = 100001 # 문제에서 주어진 최댓값은 10^5
        for i in prices:
            profit = max(profit, i - min_price)
            
            if i < min_price:
                min_price = i
        
        return profit
      
# 힙 구조 사용하기
import heapq
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 2:
            return 0
        
        heap_list = []
        for i in prices:
            heapq.heappush(heap_list, i)
            if i - heap_list[0] > profit:
                profit = i - heap_list[0]
        
        return profit
