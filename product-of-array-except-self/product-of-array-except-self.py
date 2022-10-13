class Solution:
    """"
    nums = [1,2,3,4], product of all = 1 * 2 * 3 *4 = 24, numZero = 0
    prodExcept = [24 / 1, 24/ 2, 24 / 3, 24 / 4]
    
    nums = [-1,1,0,-3,3] product of all = 9, numZero = 1
    prodExcept = [0,0,9,0,0]
    
    nums = [-1,0,0,-3,3]
    
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productOfAll = 1
        numZero = 0
        
        for num in nums:
            if num != 0:
                productOfAll *= num
            else:
                numZero += 1
                if numZero == 2:
                    break
        
        for i in range(len(nums)):
            if numZero == 2 or numZero == 1 and nums[i] != 0:
                nums[i] = 0
            elif numZero == 1:
                nums[i] = productOfAll
            else:
                nums[i] = productOfAll // nums[i]
        
        return nums
        