import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) > 1:
            score = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        else:
            return -1
        
        heapq.heappush(scoville, score)
        answer += 1
    
    return answer
