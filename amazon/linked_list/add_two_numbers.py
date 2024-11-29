# https://leetcode.com/explore/interview/card/amazon/77/linked-list/513/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # idea is to use simple math by add node per node.
    # we need to consider the "carry" value for result >= 10
    # length of the 2 node can be different also
    # so, to make it easier, if 1 of the node already reach the end, we consider it to be 0
    # we stop the process if both linked list already reach the end AND the carry already 0
    # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # Output: [8,9,9,9,0,0,0,1]
    # time complexity : O(n)
    # space complexity : O(1), we didn't count the result space
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = None
        temp = None
        while True:
            if l1 == None and l2 == None and carry == 0:
                return head

            l1_val = 0
            l2_val = 0

            if l1 != None:
                l1_val = l1.val
            
            if l2 != None:
                l2_val = l2.val

            s = l1_val + l2_val + carry
            if s >= 10:
                carry = 1
                s -= 10
            else:
                carry = 0
            
            node = ListNode(s)
            if head == None:
                head = node
                temp = node
            else:
                temp.next = node
                temp = node
            
            if l1 != None:
                l1 = l1.next
            
            if l2 != None:
                l2 = l2.next

    def print(self, l: ListNode):
        while l != None:
            print(l.val)
            l = l.next

node2 = ListNode(2)
node4 = ListNode(4)
node3 = ListNode(3)
node5 = ListNode(5)
node6 = ListNode(6)
node41 = ListNode(4)


node2.next = node4
node4.next = node3

node5.next = node6
node6.next = node41

s = Solution()

r = s.addTwoNumbers(node2, node5)
s.print(r)

