class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        sorted_inv = sorted(intervals)
        print(sorted_inv)

        i = 0
        while i != len(sorted_inv) - 1:
            if sorted_inv[i][1] >= sorted_inv[i+1][0]:
                start = min(sorted_inv[i][0], sorted_inv[i + 1][0])
                end = max(sorted_inv[i][1], sorted_inv[i + 1][1])

                sorted_inv.pop(i)
                sorted_inv[i][0] = start
                sorted_inv[i][1] = end
            else:
                i += 1

        return sorted_inv