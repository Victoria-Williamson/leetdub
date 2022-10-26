# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -2 ** 31
        
        def findMaxPath(root):
            if root == None:
                return 0
            
           
            leftSum = findMaxPath(root.left)
            rightSum = findMaxPath(root.right)
            
            # print("")
            # print(root.val)
            # print(leftSum, rightSum)
            self.maxSum = max(self.maxSum, root.val + leftSum + rightSum)
            return max(0, root.val + max(leftSum, rightSum))
            
        
        findMaxPath(root)
       
        return self.maxSum
            
        
        
        