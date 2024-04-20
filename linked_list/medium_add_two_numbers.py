# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = None
        head = None

        while True:

            if l1 == None and l2 == None and carry == 0:
                return root
            
            num1 = 0
            if l1 != None:
                num1 = l1.val
            
            num2 = 0
            if l2 != None:
                num2 = l2.val
            
            result = carry + num1 + num2
            carry = int(result / 10)
            node_result = result % 10
            
            node = ListNode(node_result)

            if root == None:    
                root = node
                head = node
            else:
                head.next = node
                head = head.next
            
            if l1 != None:
                l1 = l1.next
            
            if l2 != None:
                l2 = l2.next

            pass