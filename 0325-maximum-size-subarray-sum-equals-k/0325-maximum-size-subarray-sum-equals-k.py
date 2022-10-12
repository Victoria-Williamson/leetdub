class Solution:
    # Explanation : Two sum algorithm + prefix algorithm 
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:   
        sums = {}
        current = 0
        sol = 0
        
        for i in range(len(nums)):
            current += nums[i]
            
            if current == k:
                sol = i + 1
            
            if current - k in sums:
                sol = max(sol, i - sums[current - k ])
            
            if current not in sums:
                sums[current] = i
        return sol