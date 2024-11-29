# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # iterative
    # idea is to use queue
    # we will put the left and right of node
    # and then we pop the first element of queue
    # this way, we can get it level by level
    # to separate each level, we can rely on current size of queue
    # the current size of queue is consist by nodes within same level
    # time complexity : O(n)
    # space complexity : O(n)
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root == None:
            return []
        
        q = [root]
        result = []

        while len(q) > 0:
            q_size = len(q)
            temp = []
            for i in range(q_size):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                temp.append(node.val)
            
            result.append(temp)
        
        return result
                    
# [ A D I]

# [F] [B G]  

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

s = Solution()
result = s.levelOrder(node_F)
print(result)