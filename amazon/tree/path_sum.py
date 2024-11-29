# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # recursive
    # idea is to traverse using DFS because it will visit the children of the current node
    # this path is ned to be until the leaf, meaning until we found node with no children at all
    # we keep adding the node's value
    # that's why we will compare the value when we found the leaf
    # if right / left node is null when the other still have children, we return False for that path
    # time complexity : O(n)
    # space complexity : O(n)
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return False
        
        return self.helper(root, targetSum, 0)
    
    def helper(self, root: TreeNode, targetSum: int, currentSum: int):
        if not root:
            return False

        currentSum += root.val

        if not root.left and not root.right:
            return targetSum == currentSum
        
        return self.helper(root.left, targetSum, currentSum) or self.helper(root.right, targetSum, currentSum)

class Solution2:
    # iterative
    # idea is to traverse using pre order
    # and we keep adding the sum from node value and store it alongside with its node
    # with this we can keep track of the sum from the path
    # if we already at leaf and the sum is fulfilled, we can return immediately
    # otherwise if until queue empty the sum is not equal, we will return false
    # time complexity : O(n)
    # space complexity : O(n)
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return False
        
        currentSum = 0
        stack = [[root, currentSum]]

        while len(stack) > 0:
            node, cs = stack.pop()
            cs += node.val

            if not node.left and not node.right and cs == targetSum:
                return True
            
            if node.right:
                stack.append([node.right, cs])

            if node.left:
                stack.append([node.left, cs])
        
        return False
    pass

node1 = TreeNode(1)
node21 = TreeNode(2)
node22 = TreeNode(2)
node31 = TreeNode(3)
node32 = TreeNode(3)
node41 = TreeNode(4)
node42 = TreeNode(4)

node1.left = node21
node1.right = node22
node21.left = node31
node21.right = node41
node22.left = node41
node22.right = node31

s = Solution2()
assert s.hasPathSum(node1, 6) == True