class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = (2 ** 31) - 1
        def isValidMove(x,y):
            if x >= 0 and x < len(rooms) and y >= 0 and y < len(rooms[0]):
                return True
            return False
        
        def addAround(x,y,dist):
            if not isValidMove(x,y) or rooms[x][y] == -1:
                return 
            if dist < rooms[x][y]:
                rooms[x][y] = dist
                for xMove, yMove in [(1,0), (0,1), (-1,0), (0,-1)]:
                    addAround(xMove + x, yMove + y, dist + 1)
           
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    for xMove, yMove in [(1,0), (0,1), (-1,0), (0,-1)]:
                        addAround(i + xMove, j + yMove, rooms[i][j] + 1)
        
       
            
            
                
                
            
            
        
        