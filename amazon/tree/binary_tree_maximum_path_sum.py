# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        

        pass

nodemin10 = TreeNode(-10)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

nodemin10.left = node9
nodemin10.right = node20
node20.left = node15
node20.right = node7

s = Solution()
s.maxPathSum(nodemin10)