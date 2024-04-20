'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        queue = []
        queue.append(root)
        result = []

        while len(queue) != 0:
            root = queue.pop(0)
            result.append(root.val)
            if root.left != None:
                queue.append(root.left)
            if root.right != None:
                queue.append(root.right)
        
        return result
        pass

r = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

r.left = node9
r.right = node20
node20.left = node15
node20.right = node7

s = Solution()
s.levelOrder(r)