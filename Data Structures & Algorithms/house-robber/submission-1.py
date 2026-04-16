class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        def rH(i: int) -> int:
            if i == n - 1:
                memo[i] = nums[i]
                return memo[i]
            elif i == n - 2:
                memo[i] = max(nums[i], nums[i+1])
                return memo[i]
            else:
                if memo[i] != -1:
                    return memo[i]
                else:
                    memo[i] = max(nums[i] + rH(i+2), rH(i+1))
                    return memo[i]

        return rH(0)