# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        mid = n // 2
        left = 0
        right = n
        
        x = guess(mid)
        while (x != 0 and left < right):
            if x == 1:
                left = mid + 1
                mid = (left + right) // 2
                x = guess(mid)
            else:
                right = mid - 1
                mid = (left + right) // 2
                x = guess(mid)

        return mid
