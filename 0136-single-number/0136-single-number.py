class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singleNums = set()
        
        for num in nums:
            if num not in singleNums:
                singleNums.add(num)
            else:
                singleNums.remove(num)
        
        return singleNums.pop()