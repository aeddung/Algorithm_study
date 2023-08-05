class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        n, p, z = [], [], [] # negative, positive, zero
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num) 
        
        N, P = set(n), set(p)

        if z: # 0이 들어가 있는 경우
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))
        
        if len(z) >= 3: # 0이 3개 이상인 경우
            res.add((0, 0, 0))
        
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    # sorted 필요: tuple 형태로 정답 리스트에 들어가게 되는데, 순서가 바뀌면 다른 원소로 취급하기 때문
                    res.add(tuple(sorted([n[i], n[j], target]))) 

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))
        
        return res
