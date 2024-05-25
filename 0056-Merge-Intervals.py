class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda x: (x[0], x[1]))

        if len(intervals) == 1:
            return intervals

        currStart = intervals[0][0]
        currEnd = intervals[0][1]
        mergedIntervals = []

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start <= currEnd:
                currEnd = max(currEnd, end)
            else:
                mergedIntervals.append([currStart, currEnd])
                currStart = start
                currEnd = end
            if i == len(intervals) - 1:
                mergedIntervals.append([currStart, currEnd])

        return mergedIntervals
