class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dList = []
        
        for i in range(len(points)):
            x,y = points[i]
            d = math.sqrt((x**2) + (y **2))
            heapq.heappush(dList, (d,i))
        
        k_smallest = heapq.nsmallest(k,dList)
        smallest = []
        
        for _, index in k_smallest:
            smallest.append(points[index])
        return smallest