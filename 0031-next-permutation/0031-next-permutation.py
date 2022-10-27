class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def findNonDecreasing(index):
            while(index >= 0):
                if nums[index] < nums[index +1]:
                    return index
                index -= 1
            return -1
                       
        index = findNonDecreasing(len(nums) -2)
        if index == -1:
            nums.sort()
            return
        
        swapIndex = None
        
        for i in range(len(nums) - 1, index, -1):
            if nums[i] > nums[index] and (swapIndex == None or nums[i] - nums[index] < nums[swapIndex] - nums[index]):
                swapIndex = i
        
        print(swapIndex,index)
        temp = nums[index]
        nums[index] = nums[swapIndex]
        nums[swapIndex] = temp
        
        leftSwap, rightSwap = index + 1, len(nums) -1
        while leftSwap < rightSwap:
            temp = nums[leftSwap]
            nums[leftSwap] = nums[rightSwap]
            nums[rightSwap] = temp 
            leftSwap += 1
            rightSwap -=1
            
        """
        Do not return anything, modify nums in-place instead.
        """
        