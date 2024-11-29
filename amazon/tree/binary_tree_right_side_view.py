# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # iterative
    # idea is to use BFS with queue
    # on every level, we only interest with last node in the queue since we want to print the right side view
    # so we check if i == len_queue - 1
    # time complexity : O(n)
    # space complexity : O(n)
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        
        queue = [root]
        result = []

        while len(queue) > 0:
            len_queue = len(queue)
            for i in range(len_queue):
                node = queue.pop(0)
                if i == len_queue - 1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                pass

        return result
        pass

class Solution2:
    # recursive DFS
    # idea is to use pre order traversal but instead of go left first, we will go right first
    # this is because we want to get the most right position on each level
    # then we check if on this level, this is the first time we encounter the node
    # that must be our most right position, hence we take it
    # time complexity: O(n)
    # space complexity : O(n)
    def rightSideView(self, root: TreeNode) -> list[int]:
        result = []
        self.helper(root, 0, result)
        return result

    def helper(self, root: TreeNode, level: int, result: list):

        if not root:
            return

        if level == len(result):
            result.append(root.val)
        
        self.helper(root.right, level + 1, result)
        self.helper(root.left, level + 1, result)

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

s = Solution2()
result = s.rightSideView(node3)
print(result)