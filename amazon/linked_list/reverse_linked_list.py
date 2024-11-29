# https://leetcode.com/explore/interview/card/amazon/77/linked-list/2979/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        pass

    def print(self, l: ListNode):
        while l != None:
            print(l.val)
            l = l.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
l = s.reverseList(node1)
s.print(l)