'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        pass

    def print(self, head: ListNode):
        while head:
            print(head.val)
            head = head.next
        pass

s = Solution()

node1 = ListNode(1)
node4 = ListNode(4)
node3 = ListNode(3)
node2 = ListNode(2)
node5 = ListNode(5)
node2_1 = ListNode(2)

node1.next = node4
node4.next = node3
node3.next = node2
node2.next = node5
node5.next = node2_1

result = s.partition(node1, 3)
s.print(result)

