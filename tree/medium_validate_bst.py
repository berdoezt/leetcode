class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        pass
    pass

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    seq_data = []

    def populateData(self, node):
        if node == None:
            return
        
        self.populateData(node.left)
        self.seq_data.append(node.val)
        self.populateData(node.right)

    def isValidBST(self, root):
        self.seq_data = []
        self.populateData(root)

        if len(self.seq_data) == 0 or len(self.seq_data) == 1:
            return True
        
        for i in range(1, len(self.seq_data)):
            if self.seq_data[i] <= self.seq_data[i - 1]:
                return False
        
        return True


# r = Node(5)
# node4 = Node(4)
# node3 = Node(3)
# node6 = Node(6)
# node7 = Node(7)

# r.left = node4
# r.right = node6
# node6.left = node3
# node6.right = node7
    
r = Node(0)

s = Solution()
print(s.isValidBST(r))