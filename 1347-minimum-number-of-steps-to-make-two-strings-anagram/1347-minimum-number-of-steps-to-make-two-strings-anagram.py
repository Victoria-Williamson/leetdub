class Solution:
    def minSteps(self, s: str, t: str) -> int:
        diff = 0
        sCount = [0 for i in range(26)]
        tCount = [0 for i in range(26)]
        
        for i in range(len(s)):
            sCount[ord(s[i]) - ord('a')] += 1
            tCount[ord(t[i]) - ord('a')] += 1
        
        for i in range(26):
            diff += abs(sCount[i] - tCount[i])
        
        return diff // 2