class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if nums[l] <= nums[r]:
            return nums[l]

        while l <= r:
            mid = (l + r)//2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid