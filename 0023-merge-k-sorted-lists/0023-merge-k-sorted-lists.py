# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = None
        temp = head
        
        nodes = {}
        
        for l in lists:
            if l != None:
                if l.next == None:
                    nextVal = -1
                else:
                    nextVal = l.next.val
                nodes[len(heap)] = l
                heapq.heappush(heap, (l.val, nextVal, len(heap)))
        
        while len(heap) != 0:
            value, nextValue, nodeIndex = heapq.heappop(heap)
            
            node = nodes[nodeIndex]
            if head == None:
                head = node
                temp = node
            else:
                temp.next = node
                temp = node
            
            node = node.next
            if node != None:
                if node.next == None:
                        nextVal = -1
                else:
                    nextVal = node.next.val
                
                nodes[nodeIndex] = node
                heapq.heappush(heap, (node.val, nextVal, nodeIndex))
        return head
        