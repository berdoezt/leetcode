# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> list[int]:
        result = []
        self.leftSideViewWithoutLeaf(root, result)
        self.leaf(root, result)
        self.rightSideViewReverseWithoutLeaf(root, result)
        return result
        pass

    def leftSideViewWithoutLeaf(self, root: TreeNode, result: list):
        if not root:
            return []
        
        queue = [root]

        while len(queue) > 0:
            len_queue = len(queue)
            for i in range(len_queue):
                node = queue.pop(0)

                if node.left or node.right:
                    if i == 0:
                        result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                pass
    
    def leaf(self, root: TreeNode, result: list):
        queue = [root]

        while len(queue) > 0:
            node = queue.pop(0)
            if not node.left and not node.right:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
            pass
    
    def rightSideViewReverseWithoutLeaf(self, root: TreeNode, result: list):
        if not root:
            return []
        
        queue = [root]
        temp = []
        while len(queue) > 0:
            len_queue = len(queue)
            for i in range(len_queue):
                node = queue.pop(0)

                if node.left or node.right:
                    if i == len_queue - 1:
                        temp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                pass
        
        while len(temp) > 0:
            result.append(temp.pop())

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

result = s.boundaryOfBinaryTree(node3)
print(result)