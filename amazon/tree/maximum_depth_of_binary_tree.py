# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # iterative
    # idea is to traverse level by level like in BFS
    # we use queue since this is for BFS
    # time complexity : O(n)
    # space complexity : O(n)
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        q = [root]
        depth = 0

        while len(q) > 0:
            for i in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        
        return depth

class Solution2:
    # bottom up recursive
    # idea is to look at single node (root), the max depth is 1 (denote by no left and no right)
    # but if that node have left or right, we will repeat the process
    # once we get the left result and right result, we need to get the maximum out of the 2
    # it's because maybe the left and right have different depth
    # so that's why we return 1 + max(l, r)
    # time complexity : O(n)
    # space complexity : O(n)
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        l = 0
        if root.left:
            l = self.maxDepth(root.left)
        
        r = 0
        if root.right:
            r = self.maxDepth(root.right)
        
        return 1 + max(l, r)

# [self.depth(F, 0)]

'''
            F               --- 1
        B       G           --- 2
      A   D       I         --- 3
    C           E   H       --- 4
              J   K         --- 5
'''

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
result = s.maxDepth(node_F)
print(result)