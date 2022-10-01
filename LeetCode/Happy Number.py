class Solution:
    def isHappy(self, n: int) -> bool:
        l = []
        while True:
            num = str(n)
            n = 0
            for i in range(len(num)):
                n += (int(num[i]) ** 2)
                
            if n in l: # 무한 루프 방지
                break
                
            l.append(n)

            if n == 1:
                return True

        return False
