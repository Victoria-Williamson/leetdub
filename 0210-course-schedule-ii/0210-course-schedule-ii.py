class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        coursesRem = [0 for i in range(numCourses)]
        nextCourses = {i : [] for i in range(numCourses)}
        order = []
        seen = set()
        ready = []
        
        for preReq in prerequisites:
            nextCourses[preReq[1]].append(preReq[0])
            coursesRem[preReq[0]] += 1
                
        
        for course in range(numCourses):
            if coursesRem[course] == 0:
                ready.append(course)
        
        while ready:
            course = ready.pop(0)
            if course not in seen:
                for c in nextCourses[course]:
                    coursesRem[c] -= 1
                    if  coursesRem[c] == 0:
                        ready.append(c)
                seen.add(course)
                order.append(course)
        if len(order) != numCourses:
            return []
        return order
            
        
        
        