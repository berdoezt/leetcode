# https://leetcode.com/explore/interview/card/amazon/77/linked-list/2976/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # idea is to connect the two lists together instead of create new list
    # we iterate over all the list step by step and find which one is smaller and change the pointer to it
    # the length of the two list can be different, so if one list already reach the end, we use the default value 102 which is the biggest one
    # so the other list will always be picked up due to the comparison
    # this will be easier to manage
    # time complexity : O(m + n)
    # space complexity : O(1)
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = None
        temp = None
        while True:
            if list1 == None and list2 == None:
                return head
            
            list1_val = 102
            list2_val = 102

            if list1 != None:
                list1_val = list1.val

            if list2 != None:
                list2_val = list2.val
            
            if list1_val < list2_val:
                if head == None:
                    head = list1
                else:
                    temp.next = list1
                
                temp = list1

                if list1 != None:
                    list1 = list1.next
            else:
                if head == None:
                    head = list2
                else:
                    temp.next = list2
                
                temp = list2
                
                if list2 != None:
                    list2 = list2.next

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

node11 = ListNode(1)
node22 = ListNode(2)
node33 = ListNode(3)
node44 = ListNode(4)
node55 = ListNode(5)

node11.next = node22
node22.next = node33
node33.next = node44
node44.next = node55

s = Solution()

l = s.mergeTwoLists(node1, node11)
s.print(l)