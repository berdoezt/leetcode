
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # the task is to connect all nodes in same level
    # so given below tree, if we not connected it will print like this 1#2#4#
    # it will start from the most left on each level, and try to going to the next
    # if we didn't connect to the right, it will stop -> denotes by # symbol
    # so we need to connect by using the self.next
    # idea is we can use BFS to traverse each level with the help of queue
    # once we enter the level, we should already get all nodes in the queue ready to be connected
    # so we have pointer to current_node, and when we pop out new node from queue, we connect it and then move the curent_node
    # time complexity : O(N)
    # space complexity : O(N)
    def connect(self, root: Node) -> Node:
        if root == None:
            return root

        queue = [root]

        while len(queue) > 0:
            len_queue = len(queue)

            current_node = None
            for i in range(len_queue):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

                if current_node == None:
                    current_node = node
                    continue

                current_node.next = node
                current_node = node
        
        return root
        pass

    def print(self, root: Node):
        queue = [root]

        while len(queue) > 0:
            node = queue.pop(0)
            head = node
            while head:
                print(head.val, end="")
                head = head.next
            print("#", end="")
            if node.left:
                queue.append(node.left)
        print()
            
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.left = node2
node1.right = node3
# node2.next = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
# node4.next = node5
# node5.next = node6
# node6.next = node7

s = Solution()
node11 = s.connect(node1)
s.print(node11)