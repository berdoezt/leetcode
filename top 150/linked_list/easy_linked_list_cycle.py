# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast_head = head

        while True:
            if head == None:
                return False
            if fast_head == None:
                return False
            head = head.next
            next_fast_head = fast_head.next
            if next_fast_head == None:
                return False
            fast_head = next_fast_head.next

            if head == fast_head:
                return True

            
            
        pass

node4 = ListNode(4)
node0 = ListNode(0)
node2 = ListNode(2)
node3 = ListNode(3)

node3.next = node2
node2.next = node0
node0.next = node4
# node4.next = node2

s = Solution()

assert s.hasCycle(node3) == False

        