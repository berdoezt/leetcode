'''
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head

        length = 0
        root = head
        last = None

        while head:
            length += 1
            if head.next == None:
                last = head
            head = head.next
            pass

        if k % length == 0:
            return root

        pos = length - (k % length) - 1
        head = root

        for i in range(pos):
            head = head.next
        
        before_pos = head
        after_pos = head.next

        before_pos.next = None
        last.next = root

        return after_pos
        pass

    def print(self, head: ListNode):
        while head:
            print(head.val)
            head = head.next
        pass

s = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

result = s.rotateRight(node1, 0)
s.print(result)
