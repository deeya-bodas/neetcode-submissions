class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]
        top_k = []

        for i in range(len(nums)):
            counts[nums[i]] = 1 + counts.get(nums[i], 0)

        for key, val in counts.items():
            freq[val].append(key)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                top_k.append(n)
                if len(top_k) == k:
                    return top_k
        