class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def minCost(i: int) -> int:
            print("i is: " + str(i))
            if i >= n - 2:
                return 0
            else:
                return min(cost[i + 1] + minCost(i + 1), cost[i + 2] + minCost(i + 2))

        return minCost(-1)