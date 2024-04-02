class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        pass
    pass

def maxDepth(node: Node):
    if node == None:
        return 0

    return 1 + max(maxDepth(node.left), maxDepth(node.right))



r = Node(3)
node9 = Node(9)
node20 = Node(20)
node15 = Node(15)
node7 = Node(7)

r.left = node9
r.right = node20
node9.left = node15
node15.right = node7

print(maxDepth(r))

