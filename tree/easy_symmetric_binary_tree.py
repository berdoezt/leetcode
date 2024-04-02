# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def compare(self, nodeLeft: TreeNode, nodeRight: TreeNode) -> bool:
        if nodeLeft == None and nodeRight == None:
            return True
        
        if nodeLeft != None and nodeRight != None and nodeLeft.val == nodeRight.val:
            return self.compare(nodeLeft.left, nodeRight.right) and self.compare(nodeLeft.right, nodeRight.left)

        return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if root.left == None and root.right == None:
            return True
        
        return self.compare(root.left, root.right)

root = TreeNode(1)
node21 = TreeNode(2)
node22 = TreeNode(2)
node31 = TreeNode(3)
node32 = TreeNode(3)
node41 = TreeNode(4)
node42 = TreeNode(4)

root.left = node21
root.right = node22
node21.left = node31
node21.right = node41
node22.left = node42
node22.right = node32

s = Solution()
print(s.isSymmetric(root))
