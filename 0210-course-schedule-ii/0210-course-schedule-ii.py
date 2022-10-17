class Solution:
    def findOrder(self, numCourses: int, prereqs: List[List[int]]) -> List[int]:
        numPreqs = [0 for i in range(numCourses)]
        visited = [False for i in range(numCourses)]
        q = []
        nextCourses = {}
        
        for prereq in prereqs:
            numPreqs[prereq[0]] += 1
            
            if prereq[1] not in nextCourses:
                nextCourses[prereq[1]] = set()
            nextCourses[prereq[1]].add(prereq[0])

                
        
        for course in range(numCourses):
            if numPreqs[course] == 0:
                q.append(course)
        
        completed = []
        while q:
            course = q.pop(0)
            if not visited[course]:
                if course in nextCourses:
                    
                    for nextCourse in nextCourses[course]:
                        numPreqs[nextCourse] -= 1
                        if numPreqs[nextCourse] == 0:
                            q.append(nextCourse)
                     
                   
                completed.append(course)
                visited[course] = True
 
        if len(completed) == numCourses:
            return completed
        else:
            return []
        