class Solution:
    def __init__(self):
        self.grid = []
        self.seen = []
    
    def getValueAt(self,x,y):
        if x >= 0 and x < len(self.grid) and y >= 0 and y < len(self.grid[0]):
            return self.grid[x][y]
        else:
            return -1 
    
    def findPeakValue(self,x,y):
        possiblePeaks = []
        if self.seen[x][y]:
            return False, [x, y]
        
        self.seen[x][y] = True
        for xMove, yMove in [(1,0), (0,1)]:
            if self.getValueAt(x + xMove, y + yMove) >= self.grid[x][y]:
                possiblePeaks.append((x + xMove, y + yMove))
        
        if len(possiblePeaks) == 0:
            for xMove, yMove in [(1,0), (-1,0), (0,1), (0,-1)]:
                if self.getValueAt(x + xMove, y + yMove) >= self.grid[x][y]:
                    return False, [x, y]
            return True, [x, y]
        else:
            for newX, newY in possiblePeaks:
                isPossible, coords = self.findPeakValue(newX, newY)
                if isPossible:
                    return isPossible, coords
        
        return False, [x,y]
                
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        self.seen=[[False for i in range(len(mat[0]))] for j in range(len(mat))]
        self.grid = mat
        
        for i in range(len(mat)):
            for j in range(len(mat)):
                foundPeak, coords = self.findPeakValue(i,j)
                if foundPeak:
                    return coords
        