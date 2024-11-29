'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

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
    dups = {}

    def deleteDup(self, head: ListNode) -> ListNode:
        self.dups = {}
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
                self.dups[head.val] = True
            
            next_node = next_node.next
            pass

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        root = head
        if root == None:
            return None
        
        head_after_remove_dup = self.deleteDup(head)
        next_node = head_after_remove_dup.next

        while True:
            if next_node == None:
                head_after_remove_dup.next = next_node
                if root.val in self.dups:
                    root = root.next
                
                return root
            
            if next_node.val not in self.dups:
                head_after_remove_dup.next = next_node
                head_after_remove_dup = next_node
            
            next_node = next_node.next
            

    def print(self, head: ListNode):
        while head:
            print(head.val)
            head = head.next
        pass

s = Solution()

node1 = ListNode(1)
node11 = ListNode(1)
node12 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node11
node11.next = node12
node12.next = node2
node2.next = node3

head = s.deleteDuplicates(node1)
s.print(head)           