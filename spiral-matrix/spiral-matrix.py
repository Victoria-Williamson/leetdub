class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seen = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        moves = [(0,1),(1,0), (0,-1), (-1,0)]
        order = []
        rem = len(matrix) * len(matrix[0])
        mIndex = 0
        x = 0
        y = 0
        
        def isValid(x,y):
            if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and not seen[x][y]:
                return True
            return False
        
        def setViewed(x,y):
            order.append(matrix[x][y])
            seen[x][y] = True
            
        
        setViewed(x,y)
        rem -= 1
        while rem != 0:
            xx, yy = moves[mIndex]
            
            while isValid(x + xx,y + yy):
                x += xx
                y += yy
                setViewed(x,y)
                rem -= 1
            
            mIndex = (mIndex + 1) % 4
            
            xx, yy = moves[mIndex]
            if not isValid(x + xx,y + yy):
                break
        return order
            
                
            
            
        