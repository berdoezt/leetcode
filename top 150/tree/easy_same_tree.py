class Solution:
    def isSameTree(self, p, q) -> bool:
        if p == None and q == None:
            return True
        
        if p != None and q!= None and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False