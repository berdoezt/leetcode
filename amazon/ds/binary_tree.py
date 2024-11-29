# non linear data structure

# each node has at most 2 children node
# top-most is called root
# bottom-most is called leaf

# binary tree
# - data
# - node left
# - node right

# traversal
# - bfs : breadth first search, level by level
# - dfs : depth first search, go deep to leaf , and go up and move to another branch
    # - pre order : visit node, go left, go right
    # - in order : go left, visit node, go right
    # - post order : go left, go right, visit node

# advantage
# - searching element takes O(log n) which is faster than linked list O(n)

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        pass

class BinaryTree:
    def __init__(self):
        self.root = None
        pass

    def pre_order_iterative(self, node) -> list:
        # use stack
        s = [node]
        result = []

        while len(s) > 0:
            n = s[len(s) - 1]
            result.append(s.pop(len(s) - 1).data)

            if n.right != None:
                s.append(n.right)
            
            if n.left != None:
                s.append(n.left)

        return result
    
    def pre_order_recursive(self, node) -> list:
        result = []
        self.pre_order_recursive_helper(node, result)
        return result
        pass

    def pre_order_recursive_helper(self, node, result):
        if node == None:
            return
        
        result.append(node.data)
        self.pre_order_recursive_helper(node.left, result)
        self.pre_order_recursive_helper(node.right, result)

    def in_order_iterative(self, node):
        s = [node]
        result = []

        while len(s) > 0:
            print(s)
            node = s[len(s) - 1]
            if node.left != None:
                s.append(node.left)
            else:
                n = s.pop(len(s) - 1)
                result.append(n.data)
                if n.right != None:
                    s.append(n.right)

        return result

    def post_order(self, node):
        pass

'''

            A
        B       C
     D    E    F  G

    [D B E ]

    [A B D ]
'''
node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")
node_I = Node("I")

node_F.left = node_B
node_F.right = node_G
node_B.left = node_A
node_B.right = node_D
node_D.left = node_C
node_D.right = node_E
node_G.right = node_I
node_I.left = node_H

b = BinaryTree()
assert b.pre_order_recursive(node_F) == b.pre_order_iterative(node_F)
print(b.in_order_iterative(node_F))
# print(result)
