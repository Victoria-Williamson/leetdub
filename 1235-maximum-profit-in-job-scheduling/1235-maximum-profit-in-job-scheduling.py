class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        paths = {}
        jobs = []
        maxProfits = []
        
        maxProfit = 0
        
        for i in range(len(endTime)):
            heapq.heappush(jobs,(startTime[i], i))
            maxProfit = max(maxProfit, profit[i])
            
        
        end, index = heapq.heappop(jobs)
        paths[endTime[index]] = profit[index]
        maxProfits.append((-1 * profit[index], endTime[index]))
        
        while len(jobs) != 0:
            start, index = heapq.heappop(jobs)
            added = False
            
            tprofits = maxProfits.copy()
            maxProfits = []
            while len(tprofits) > 0:
                profits, end = heapq.heappop(tprofits)
                profits *= -1
                if end <= start:
                    heapq.heappush(maxProfits, (-1 * (profits + profit[index]), endTime[index]))
                    maxProfit = max(maxProfit, profits + profit[index])
                    heapq.heappush(maxProfits, (-1 * profits, end))
                    break
                else:
                    heapq.heappush(maxProfits, (-1 * profits, end))
#             for end in sorted(paths.keys(), reverse=True):
#                 profits = paths[end]
#                 if end <= start:
#                     if endTime[index] not in paths:
#                         paths[endTime[index]] = 0
#                     paths[endTime[index]] = max(paths[endTime[index]], profits + profit[index])
#                     maxProfit = max(maxProfit,  profits + profit[index])
                    
#                     added = True
#                 else:
#                     break
            
            if not added:
                heapq.heappush(maxProfits, (-1 * (profit[index]), endTime[index]))
                # if endTime[index] not in paths:
                #     paths[endTime[index]] = 0
                # paths[endTime[index]] = max(paths[endTime[index]], profit[index])
        print(maxProfits)
        return maxProfit
        
            
           
            
            
        
        
        