import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        nums.sort(reverse=True)
        for i in range(0, min(k, len(nums))):
            heapq.heappush(self.min_heap, nums[i])


    def add(self, val: int) -> int:
        if(len(self.min_heap) != self.k):
            heapq.heappush(self.min_heap, val)
        elif(self.min_heap[0] < val):
            heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0]
        
