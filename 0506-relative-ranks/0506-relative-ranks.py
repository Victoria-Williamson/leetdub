import heapq 

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        
        for i in range(len(score)):
            heapq.heappush(heap, ((-1 *score[i]),i))
        
        rank = 1
        
        while len(heap) != 0:
            _, index = heapq.heappop(heap)
            
            if rank == 1:
                score[index] = "Gold Medal"
            elif rank == 2:
                score[index] = "Silver Medal"
            elif rank == 3:
                score[index] = "Bronze Medal"
            else:
                score[index] = str(rank)
            
            rank += 1
        return score