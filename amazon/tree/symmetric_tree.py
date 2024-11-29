# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # iterative
    # idea is similar to BFS using queue
    # so symmetric is like putting mirror in the middle of the tree and compare the opposite
    # so for each level we need to compare between (first_node.left and second_node.right) and (first_node.right and second_node.left)
    # we also need to take care of null as well from a particular side
    # in case the first node is null and other is not or vice versa, we should return False, meaning its not the same
    # time complexity : O(n)
    # space complexity : O(n)
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        q = [root.left, root.right]

        while len(q) > 0:
            first_node = q.pop(0)
            second_node = q.pop(0)

            if not first_node and second_node:
                return False
            
            if not second_node and first_node:
                return False
            
            if not first_node and not second_node:
                continue

            if first_node.val != second_node.val:
                return False
            
            q.append(first_node.left)
            q.append(second_node.right)
            q.append(first_node.right)
            q.append(second_node.left)
            
            pass

        return True

class Solution2:
    # recursive
    # idea is to divide the tree into to parts, left and right. 
    # This is because we call symmetric when we put mirror in the middle
    # now there are node1 (left) and node2 (right)
    # for each step, we compare node1.left with node2.right and node1.right with node2.left
    # because its the definition of symmetric
    # once we found out the value is different, or node is null when other's is not null, we return False
    # we keep processing until we found null for both side, meaning we reach the end and all is symmetric
    # time complexity : O(n)
    # space complexity: O(n)
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        if not root.left and not root.right:
            return True
        
        return self.helper(root.left, root.right)

    def helper(self, node1: TreeNode, node2: TreeNode):
        if not node1 and not node2:
            return True
        
        if (not node1 and node2) or (not node2 and node1):
            return False
        
        if node1.val != node2.val:
            return False
        
        return self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)
        
        pass
'''
q = []

node21

node22


                    A
                B       C
            D      G  H    I 
        E     L          J    K
    F

q = [G H]

D
I



'''


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

result = s.isSymmetric(node1)
assert result == True