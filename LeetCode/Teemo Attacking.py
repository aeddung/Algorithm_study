# runtime: 267ms
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        answer = duration
        interval = [timeSeries[0], timeSeries[0] + duration - 1]
        for t in timeSeries[1:]:
            if t <= interval[-1]:
                answer += duration - (interval[-1] - t + 1)
            else:
                answer += duration
            interval = [t, t + duration - 1]

        return answer

# runtime: 260ms      
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        time = 0

        for i in range(n - 1):
            effect_duration = min(duration, timeSeries[i + 1] - timeSeries[i])
            time += effect_duration

        time += duration

        return time      
