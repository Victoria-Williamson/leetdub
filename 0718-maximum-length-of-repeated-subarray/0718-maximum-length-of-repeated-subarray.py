class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        self.maxLength = 0
        
        dp = [[0 for i in range(len(nums2) + 1)] for j in range(len(nums1) + 1)]
        
        sol = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                    sol = max(dp[i + 1][j + 1],sol )
        
        return sol
                
                
                
        