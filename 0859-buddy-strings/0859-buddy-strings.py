class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        misplaced = None
        misplacedLoc = None
        swapped = False
        seen = set()
        repeat = set()
        
        for i in range(len(s)):
            if s[i] in seen:
                repeat.add(s[i])
            else:
                seen.add(s[i])
            
            if s[i] != goal[i]:
                if swapped:
                    return False
                elif misplaced == None:
                    misplaced = s[i]
                    misplacedLoc = i
                elif misplaced != None:
                    if misplaced == goal[i] and s[i] == goal[misplacedLoc]:
                        swapped = True
                    else:
                        return False
        if misplaced != None and not swapped:
            return False
        return len(repeat) != 0 or swapped
        