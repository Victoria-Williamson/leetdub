class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
    
    def balanceList(self):
        if len(self.left) > len(self.right):
            oldLeft = heapq.heappop(self.left)
            heapq.heappush(self.right, -1 * oldLeft)
        elif len(self.right) - len(self.left) > 1:
            oldRight = heapq.heappop(self.right)
            heapq.heappush(self.left, -1 * oldRight)
        
    def addNum(self, num: int) -> None:
        if len(self.right) == 0 and len(self.left) == 0:
            self.right.append(num)
        elif len(self.left) == 0:
            if num > self.right[0]:
                oldRight = heapq.heappop(self.right)
                heapq.heappush(self.right, num)
                heapq.heappush(self.left, -1 * oldRight)
                
            else:
                heapq.heappush(self.left, -1 * num)
        elif len(self.right) == 0:
            if num < -1 * self.left[0]:
                oldLeft = heapq.heappop()
                heapq.heappush(self.left, num * - 1)
                heapq.heappush(self.right, -1 * oldLeft)
            else:
                heapq.heappush(self.right, -1 * num)
        else:
            if num < self.right[0]:
                heapq.heappush(self.left, - 1 * num)
               
            else:
                heapq.heappush(self.right, num)
        self.balanceList()
              
    def findMedian(self) -> float:
        if (len(self.right) + len(self.left)) % 2 == 1:
            return self.right[0]
        else:
            return ((self.right[0]) + (-1 * self.left[0])) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()