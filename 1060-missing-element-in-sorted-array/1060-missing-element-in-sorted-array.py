class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        prevMissing = 0
        for i in range(1, len(nums)):
            missing = (nums[i] - nums[i-1]) - 1
            
            if prevMissing + missing >= k:
                if prevMissing + missing == k:
                    return nums[i-1] + missing
                else:
                    return nums[i-1] + ( k - prevMissing )
            prevMissing += missing
            
        
        return nums[-1] + (k - prevMissing)
            
        
        