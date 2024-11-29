# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # iterative using stack
    # idea is similar to in order
    # we need to keep track of the node that already visited so it won't trap in endless loop
    # time complexity : O(n)
    # space complexity : O(n)
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if root == None:
            return []
        
        stack = [root]
        result = []
        visited = {}

        while len(stack) > 0:
            current_node = stack[len(stack) - 1]
            if current_node.left and (current_node.left not in visited or visited[current_node.left] == False):
                stack.append(current_node.left)
            elif current_node.right and (current_node.right not in visited or visited[current_node.right] == False):
                stack.append(current_node.right)
            else:
                current_node = stack.pop()
                result.append(current_node.val)
                visited[current_node] = True

            pass

        return result

class Solution2:
    # recursive
    # time complexity : O(n)
    # space complexity : O(n)
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        self.postorder(root, result)
        return result
        pass

    def postorder(self, root: TreeNode, result: list):
        if root == None:
            return
        
        self.postorder(root.left, result)
        self.postorder(root.right, result)
        result.append(root.val)
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
result = s.postorderTraversal(node_F)
print(result)