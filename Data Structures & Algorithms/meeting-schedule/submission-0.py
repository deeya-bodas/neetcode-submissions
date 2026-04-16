"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        def mergeSort(ints: List[Interval]) -> List[Interval]:
            if len(ints) <= 1:
                return ints
            
            mid = len(ints) // 2
            left = mergeSort(ints[0:mid])
            right = mergeSort(ints[mid:])

            return merge(left, right)

        def merge(left: List[Interval], right: List[Interval]) -> List[Interval]:
            arr = []
            li = 0
            ri = 0

            while li < len(left) and ri < len(right):
                if left[li].start <= right[ri].start:
                    arr.append(left[li])
                    li += 1
                else:
                    arr.append(right[ri])
                    ri += 1

            while li < len(left):
                arr.append(left[li])
                li += 1
            while ri < len(right):
                arr.append(right[ri])
                ri += 1

            return arr

        sorted_ints = mergeSort(intervals)

        for i in range(len(sorted_ints) - 1):
            if sorted_ints[i+1].start < sorted_ints[i].end:
                return False

        return True


