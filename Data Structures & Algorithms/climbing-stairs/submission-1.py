class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(1, n):
            temp = a + b
            a = b
            b = temp
        return b
        