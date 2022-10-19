class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [[-1 * profit[i], difficulty[i]] for i in range(len(profit))]
        heapq.heapify(jobs)
        for i in range(len(worker)):
            worker[i] *= -1
        heapq.heapify(worker)
        profits = 0
        while jobs:
            profit, difficulty = heapq.heappop(jobs)
            
            while worker and difficulty <= -1 * worker[0]:
                w = heapq.heappop(worker)
                profits -= profit
        return profits
            
            
        
        