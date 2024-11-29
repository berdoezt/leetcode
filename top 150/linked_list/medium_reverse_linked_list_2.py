'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode, tail: ListNode) -> ListNode:
        prev_node = None

        while head != tail:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
            pass

        return prev_node

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        counter = 1
        root = head
        before_node = None
        after_node = None
        left_node = None
        right_node = None

        while True:
            if counter == left - 1:
                before_node = head
            
            if counter == left:
                left_node = head
                pass
            
            if counter == right:
                right_node = head
                pass

            if counter == right + 1:
                after_node = head
                break
            
            head = head.next
            counter += 1

        self.reverseList(left_node, after_node)
        if before_node == None:
            root = right_node
        else:
            before_node.next = right_node

        left_node.next = after_node
        
        return root

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

head = s.reverseBetween(node1, 1, 3)
s.print(head)