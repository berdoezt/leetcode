# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # for each of node, calculate the height from left and height from right
    # sum it + 1 (the node itself) then if greater than current max_diameter, we update the answer
    # we traverse from top root down to the leaf to check if it has better diameter value
    # there's repeating process for calculate the height
    # because we traverse from the top to find the height, each time we going down, we need to process again to find the height
    # which means, for n nodes, we repeat n times
    # time complexity : O (n^2)
    # space complexity : O(n)
    def __init__(self):
        self.max_diameter = 0

    def height(self, node: TreeNode):
        if not node:
            return 0
        
        l = self.height(node.left)
        r = self.height(node.right)
        return 1 + max(l, r)
        pass

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.helper(root)
        return self.max_diameter - 1
        pass
    
    def helper(self, root: TreeNode):
        if root == None:
            return
        
        l_height = self.height(root.left)
        r_height = self.height(root.right)

        diameter = 1 + l_height + r_height
        self.max_diameter = max(self.max_diameter, diameter)

        self.helper(root.left)
        self.helper(root.right)
        pass

class Solution2:
    # idea is similar to solution above
    # but now when we get the height of tree, we will calculate the diameter directly from the bottom
    # so this will be more efficient than above Solution. In above solution, we start from the top to calculate the diameter
    # hence it will get the height of children everytime which cause O(n^2) complexity
    # In this one, once we get the height from the latest child, we calculate the diameter
    # so its more like the bottom up approach
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.helper(root)
        return self.max_diameter - 1
        pass
    
    def helper(self, root: TreeNode):
        if root == None:
            return 0
        
        l = self.helper(root.left)
        r = self.helper(root.right)

        diameter = 1 + l + r
        self.max_diameter = max(self.max_diameter, diameter)

        return 1 + max(l, r)
        
        pass

node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)

node3.left = node5
node3.right = node1
node5.left = node6
node5.right = node2
node2.left = node7
node2.right = node4
node1.left = node0
node1.right = node8

s = Solution()

s.diameterOfBinaryTree(node3)