'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?


'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode, tail: ListNode=None) -> ListNode:
        prev_node = None

        while head != tail:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
            pass

        return prev_node
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head_after_reverse = self.reverseList(head)
        if n == 1:

            return self.reverseList(head_after_reverse.next)
        else:
            root = head_after_reverse
            counter = 2
            next_node = head_after_reverse.next

            while True:
                if counter == n:
                    head_after_reverse.next = next_node.next
                    break

                head_after_reverse = next_node
                next_node = next_node.next
                counter += 1

            return self.reverseList(root)

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

head = s.removeNthFromEnd(node1, 5)
s.print(head)     