"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def __init__(self):
        self.mergedSchedule = None
        
    def mergeSchedule(self, schedule):
        if self.mergedSchedule == None:
            self.mergedSchedule = schedule
            return
        
        mIndex = 0
        sIndex = 0
        
        # If there are any shifts before the current earliest, add all of those in
        while sIndex < len(schedule) and mIndex < len(self.mergedSchedule):
            if schedule[sIndex].end < self.mergedSchedule[mIndex].start:
                self.mergedSchedule.insert(mIndex,schedule[sIndex])
                sIndex += 1
                mIndex += 1
            else:
                break
        
        # Merge into the remaining current schedule
        while sIndex < len(schedule) and mIndex < len(self.mergedSchedule):
            # Is after the current interval
            if schedule[sIndex].start > self.mergedSchedule[mIndex].end:
                mIndex += 1
            # Overlaps in the front or completly
            elif schedule[sIndex].start <=  self.mergedSchedule[mIndex].start and schedule[sIndex].end >= self.mergedSchedule[mIndex].start:
                self.mergedSchedule[mIndex].start = min(self.mergedSchedule[mIndex].start, schedule[sIndex].start)
                self.mergedSchedule[mIndex].end = max(self.mergedSchedule[mIndex].end, schedule[sIndex].end)
                
                while mIndex - 1 >= 0 and self.mergedSchedule[mIndex].start <= self.mergedSchedule[mIndex - 1].end:
                    self.mergedSchedule[mIndex].start = min(self.mergedSchedule[mIndex -1].start,self.mergedSchedule[mIndex].start)
                    self.mergedSchedule.pop(mIndex - 1)
                    mIndex -= 1
                while mIndex + 1 < len(self.mergedSchedule) and self.mergedSchedule[mIndex].end >= self.mergedSchedule[mIndex + 1].start:
                    self.mergedSchedule[mIndex].end = max(self.mergedSchedule[mIndex + 1].end,self.mergedSchedule[mIndex].end)
                    self.mergedSchedule.pop(mIndex+1)
                sIndex += 1
            # Overlaps at the end
            elif schedule[sIndex].start >= self.mergedSchedule[mIndex].start:
                self.mergedSchedule[mIndex].start = min(self.mergedSchedule[mIndex].start, schedule[sIndex].start)
                self.mergedSchedule[mIndex].end = max(self.mergedSchedule[mIndex].end, schedule[sIndex].end)
                
                while mIndex + 1 < len(self.mergedSchedule) and self.mergedSchedule[mIndex].end >= self.mergedSchedule[mIndex + 1].start:
                    self.mergedSchedule[mIndex].end = max(self.mergedSchedule[mIndex + 1].end,self.mergedSchedule[mIndex].end)
                    self.mergedSchedule.pop(mIndex+1)
                 
                sIndex += 1
            else:
                self.mergedSchedule.insert(mIndex,schedule[sIndex])
                sIndex += 1
                # mIndex += 1
        
        while sIndex < len(schedule):
            self.mergedSchedule.append(schedule[sIndex])
            sIndex += 1
        
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        for s in schedule:
            self.mergeSchedule(s)
           
        
        sol = []
        for i in range(1, len(self.mergedSchedule)):
            sol.append(Interval(self.mergedSchedule[i-1].end, self.mergedSchedule[i].start))
        return sol
        
        