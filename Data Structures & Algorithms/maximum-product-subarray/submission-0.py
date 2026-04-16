class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curr_min, curr_max = 1, 1
        max_prod = max(nums)

        for n in nums:
            if n == 0:
                curr_min, curr_max = 1, 1
            
            tmp = curr_min*n
            curr_min = min(curr_min * n, curr_max * n, n)
            curr_max = max(tmp, curr_max * n, n)

            max_prod = max(max_prod, curr_max)

        return max_prod