class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0] * (n + 1)
        for i in range(1, n + 1):
            counter[i] = counter[i >> 1] + (i % 2) # 비트 연산자(>>): bit 단위로 오른쪽으로 bit 단위 밀기 연산 실시

        return counter
