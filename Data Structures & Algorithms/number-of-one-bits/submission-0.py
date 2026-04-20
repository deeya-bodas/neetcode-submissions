class Solution:
    def hammingWeight(self, n: int) -> int:
        ham_weight = 0
        while n > 0:
            if n % 2 == 1:
                ham_weight += 1
            n = n // 2

        return ham_weight