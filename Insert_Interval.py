class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        results, position = [], 0

        for i in intervals:
            start, end = i.start, i.end
            if newInterval.start > end:
                results.append(i)
                position += 1
            elif newInterval.end < start:
                results.append(i)
            else:
                newInterval.start = min(start, newInterval.start)
                newInterval.end = max(end, newInterval.end)

        results.insert(position, newInterval)
        return results
