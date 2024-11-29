# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # iterative using stack
    # idea is since pre order is (visit, go left, go right)
    # left node will be visitted first
    # since stack using LIFO, we will put the right node first then the left one
    # so left node will be pickup first
    # time complexity : O(n)
    # space complexity : O(n)
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if root == None:
            return []
        result = []
        stack = [root]

        while len(stack) != 0:
            node = stack.pop(len(stack) - 1)
            result.append(node.val)

            if node.right != None:
                stack.append(node.right)

            if node.left != None:
                stack.append(node.left)

        return result

class Solution2:
    # using recursive
    # idea is at very small tree (1 root and 2 leaf only)
    # we need to visit, go left, and then go right
    # we repeat the process of every subtree until its None
    # time complexity : O(n)
    # space complexity : O(n)
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        self.preorderHelper(root, result)
        return result
        pass

    def preorderHelper(self, root: TreeNode, result: list) -> list[int]:
        if root == None:
            return
        
        result.append(root.val)
        self.preorderHelper(root.left, result)
        self.preorderHelper(root.right, result)
    

class Solution3:
    # using Morris traversal
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        pass

node_A = TreeNode("A")
node_B = TreeNode("B")
node_C = TreeNode("C")
node_D = TreeNode("D")
node_E = TreeNode("E")
node_F = TreeNode("F")
node_G = TreeNode("G")
node_H = TreeNode("H")
node_I = TreeNode("I")

node_F.left = node_B
node_F.right = node_G
node_B.left = node_A
node_B.right = node_D
node_D.left = node_C
node_D.right = node_E
node_G.right = node_I
node_I.left = node_H

s = Solution2()
result = s.preorderTraversal(node_F)
print(result)