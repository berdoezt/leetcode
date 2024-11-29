# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # iterative using stack
    # idea is similar to pre order
    # but now we need to always push left if node have left
    # also we need to mark the node that we already take out from stack as visited
    # this to prevent we push the same node again
    # time complexity : O(n)
    # space complexity : O(n)
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if root == None:
            return []
        
        stack = [root]
        result = []
        visited = {}

        while len(stack) > 0:
            current_node = stack[len(stack) - 1]
            if current_node.left and (current_node.left not in visited or visited[current_node.left] == False):
                stack.append(current_node.left)
            else:
                node = stack.pop()
                result.append(node.val)
                visited[node] = True
                if node.right:
                    stack.append(node.right)
        
        return result

class Solution2:
    # recursion
    # time complexity : O(n)
    # space complexity : O(n)
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        self.inorder(root, result)
        return result
        pass    
    
    def inorder(self, root: TreeNode, result: list) -> list[int]:
        if root == None:
            return
        
        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)

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
result = s.inorderTraversal(node_F)
print(result)