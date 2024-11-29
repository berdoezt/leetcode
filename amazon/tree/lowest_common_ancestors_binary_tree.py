# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursive
    # https://www.youtube.com/watch?v=_-QHfMDde90
    # idea is to traverse the p node or q node, once we found them, we will track back to find the lowest common ancestors
    # if we found the p or q, we will return the node
    # if not, we will keep traverse until we reach end (root = None) and return None
    # now if one of left or right is not None, we return it
    # if both of left and right is not None, meaning we have found the first occurence from backtrack as the ancestor
    # which means, this is the lowest common ancestors
    # hence now we return it
    # we keep doing this until we trackback to the top root
    # Note: One thing to be concerned is that in case of one of the node is also the lowest common ancestors for both node
    # in that case, below approach is still work because it means both node are in same subtree
    # hence, returning that node only will be the correct answer
    # time complexity : O(n)
    # space complexity : O(n)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return root
        
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and right:
            return right
        
        if not right and left:
            return left
        
        if not left and not right:
            return None
        
        return root

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

result = s.lowestCommonAncestor(node3, node5, node1)
assert result == node3

result = s.lowestCommonAncestor(node3, node5, node4)
assert result == node5
