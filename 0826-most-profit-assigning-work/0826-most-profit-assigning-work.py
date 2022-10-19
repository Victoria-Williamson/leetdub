class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [[-1 * profit[i], difficulty[i]] for i in range(len(profit))]
        heapq.heapify(jobs)
        
        worker.sort(reverse=True)
        
        profits = 0
        while jobs and worker:
            profit, difficulty = heapq.heappop(jobs)
            
            while worker and difficulty <=  worker[0]:
                w = worker.pop(0)
                profits -= profit
        return profits
            
            
        
        