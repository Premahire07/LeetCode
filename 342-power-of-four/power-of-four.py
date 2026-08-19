class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n == 1:
            return True

        while n >= 4:
            if n % 4 == 0:
                n = n // 4
            else:
                return False

        return n == 1