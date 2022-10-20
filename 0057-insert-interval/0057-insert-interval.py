class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        
        merged = [intervals[0]]
        
        for interval in intervals[1:]:
            if merged[-1][1] >= interval[0]:
                merged[-1] = [min(merged[-1][0],interval[0]), max(merged[-1][1], interval[1])]
            else:
                merged.append(interval)
        return merged
                
        