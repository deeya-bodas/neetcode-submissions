class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * n
        def minCost(i: int) -> int:
            if i >= n - 2:
                memo[i] = 0
                return memo[i]
            else:
                if memo[i] != -1:
                    return memo[i]
                else:
                    memo[i] = min(cost[i + 1] + minCost(i + 1), cost[i + 2] + minCost(i + 2))
                    return memo[i]

        return minCost(-1)