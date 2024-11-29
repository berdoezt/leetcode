# linear data structure

# data stored not at a contigous location, 
# but it spread across location and connected by pointer to the location
# data is represent by node which contain the adress of the next node to create a linked list

# node -> node -> node

# node
# - data : the value
# - next : the memory adress of next node
# - head : pointer to the first node

# advantage:
# - dynamic data structure : size of memory can be allocated/deallocated at run time 
# - ease of insertion / deletion : simpler than array since no element need to be shifted after insert / deletion. Just update the address
# - efficient memory utilizationn : due to dyanmic data structure, the increase or decrease of memory is per the requirement so avoid waste memory
# - implementation : various advanced data structured implemented using linked list. Example : hash map, stack, queue, graph

# disadvantage:
# - extra memory : need extra memory to store pointer next and / or prev
# - random access : unliked arrays, linked list element can't be accessed via index. Require traverse to access the element

# types:
# - single linked list : traversing in forward direction, only 1 direction.
# - double linked list : traversing in forward and backward direction, have next pointer and prev pointer
# - circular linked list : last node point back to the first node, create a cyclic. Can be applied on single / double linked list

# operation
# - insert : done by adjusting the pointer to new node, and new node to the next node / null
# - delete : done by pointing the neighbour node to the next node
# - search : traverse from the head until get the value

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            
            temp.next = node
    
    def insert(self, node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def insertAtIndex(self, idx, node):
        if self.head == None:
            self.head = node
            return

        end = self.head
        prev = self.head
        for i in range(idx):
            if end == None:
                break

            prev = end
            end = end.next
        
        if prev == self.head:
            self.insert(node)
        else:

            node.next = end
            prev.next = node
    
    def deleteFront(self):
        if self.head == None:
            return

        self.head = self.head.next
        pass

    def deleteLast(self):
        if self.head == None:
            return
        
        end = self.head
        prev = self.head
        while end.next != None:
            prev = end
            end = end.next

        if prev == self.head:
            self.deleteFront()
        else:
            prev.next = end.next
        pass

    def deleteAtIndex(self, idx):
        if self.head == None:
            return

        end = self.head
        prev = self.head

        for i in range(idx):
            if end.next == None:
                break

            prev = end
            end = end.next

        if prev == self.head:
            self.deleteFront()
        else:
            prev.next = end.next

    def length(self):
        temp = self.head
        result = 0

        while temp != None:
            result += 1
            temp = temp.next
        
        return result

    def length_with_recursive(self):
        return self.l(self.head)

    def l(self, node):
        if node == None:
            return 0
        else:
            return 1 + self.l(node.next)
    
    def is_value_exist(self, val):
        temp = self.head

        while temp != None:
            if temp.data == val:
                return True
            temp = temp.next
        
        return False
        pass
    
    def print(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
            

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

l = SingleLinkedList()
# l.deleteFront()
l.append(node1)
l.append(node2)
l.append(node3)
l.append(node4)
l.append(node5)
l.append(node6)
l.insert(node7)
l.deleteAtIndex(1000)
print(l.is_value_exist(40))
print(l.length())
# l.insertAtIndex(7, node8)
# l.insertAtIndex(0, node9)
# l.print()
l.deleteFront()
print(l.length())
print(l.length_with_recursive())
# l.deleteLast()
# l.deleteLast()
# l.print()