class Solution:
    def hammingWeight(self, n: int) -> int:
    
        n = str(bin(n))
        num = 0 

        for i in range(len(n)):
            if n[i] == "1":
                num += 1
        return num
        