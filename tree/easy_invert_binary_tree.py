class Solution:
    def invertTree(self, root):
        if root == None:
            return root
        temp = root.left
        root.left = root.right
        root.right= temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root