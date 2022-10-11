class Solution:
    def __init__(self):
        self.prereqs = {}
        self.timeToComplete = []
        self.times = []
        
    def findTimeToComplete(self,course):
        print("Visiting", course)
        if self.timeToComplete[course] != -1:
            return 0
        
        if course not in self.prereqs:
            self.timeToComplete[course] = self.times[course]
            return self.times[course]
        
        timeToComplete = 0
        for prereq in self.prereqs[course]:
            if not self.timeToComplete[prereq] != -1 and prereq in self.prereqs:
                timeToComplete = max(timeToComplete, self.findTimeToComplete(prereq))
            elif not self.timeToComplete[prereq] != -1:
                timeToComplete = max(timeToComplete, self.times[prereq])
                self.timeToComplete[prereq] = self.times[prereq]
            elif self.timeToComplete[prereq] != -1:
                timeToComplete = max(timeToComplete, self.timeToComplete[prereq])
        
       
        self.timeToComplete[course] = timeToComplete + self.times[course]
        
        print(course, timeToComplete + self.times[course])
        return timeToComplete + self.times[course]
    
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        # Create adjacency list for any prereqs
        for relation in relations:
            if relation[1] in self.prereqs:
                self.prereqs[relation[1]].append(relation[0])
            else:
                self.prereqs[relation[1]] = [relation[0]]
        
        # Initilize Times Array
        self.times.append(0)
        self.times.extend(time)
        
        # Initilize Completed Array
        self.timeToComplete = [-1 for i in range(n + 1)]
        
        totalTime = 0
        for course in range(1, n + 1):
            totalTime = max(totalTime, self.findTimeToComplete(course))
        
        return totalTime
        
        
        
        