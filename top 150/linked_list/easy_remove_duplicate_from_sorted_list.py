'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        root = head
        if root == None:
            return None

        next_node = head.next
        while True:
            if next_node == None:
                head.next = next_node
                return root
            
            if next_node.val != head.val:
                head.next = next_node
                head = next_node
            else:
                next_node = next_node.next
            pass
    
    def print(self, head: ListNode):
        while head:
            print(head.val)
            head = head.next
        pass

s = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node31 = ListNode(3)
node32 = ListNode(3)
node41 = ListNode(4)
node42 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node31
node31.next = node32
node32.next = node41
node41.next = node42
node42.next = node5

head = s.deleteDuplicates(node1)
s.print(head)