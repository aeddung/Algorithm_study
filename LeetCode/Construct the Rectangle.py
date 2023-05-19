# runtime: 2206ms
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = int(math.sqrt(area))
        length = int(math.ceil(area / width))

        while width * length != area:
            if width * length < area:
                length += 1
            else:
                width -= 1
        
        return [length, width]

# runtime: 53ms      
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(area ** 0.5), 0, -1):
            if area % i == 0:
                return [area // i, i]
