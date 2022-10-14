import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        filledRooms = []
        roomsNeeded = 0
        
        intervals.sort()
        
      
        for interval in intervals:
            
            if len(filledRooms) > 0:
               
                end, _ = filledRooms[0]
                while end <= interval[0]:
                    heapq.heappop(filledRooms)
                    if len(filledRooms) != 0:
                        end, _ = filledRooms[0]
                    else:
                        break
                
            heapq.heappush(filledRooms,(interval[1], interval[0]))
            roomsNeeded = max(len(filledRooms), roomsNeeded)
           
           
        return roomsNeeded
    
        