class Solution:
   
    def canFinish(self, numCourses: int, prereqs: List[List[int]]) -> bool:
       # Topological Sort
       # 1. Find how many values before each course has and create a map that has 
            # before value -> after value
       # 2. Determine any courses that have no prereqs, and add to a queue
       # 3. For each value, more it as visited, and decrease the number of prereqs for each
           # If a course now has 0 prereqs add it to the list
        
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
        
        completed = 0
        while q:
            course = q.pop(0)
            if not visited[course]:
                if course in nextCourses:
                    
                    for nextCourse in nextCourses[course]:
                        numPreqs[nextCourse] -= 1
                        if numPreqs[nextCourse] == 0 and not visited[nextCourse]:
                            q.append(nextCourse)
                     
                   
                completed += 1
                visited[course] = True
 
        return completed == numCourses
                
        
            
        