class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [[profit[i], difficulty[i]] for i in range(len(profit))]
        jobs.sort(reverse=True)
        
        worker.sort(reverse=True)
        
        profits = 0
        while jobs and worker:
            profit, difficulty = jobs.pop(0)
            
            while worker and difficulty <=  worker[0]:
                w = worker.pop(0)
                profits += profit
        return profits
            
            
        
        