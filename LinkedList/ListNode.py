class ListNode: 
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next

    def reverseList(self, head): 
        if head is None:
            print("List is empty")
            return None

        def _reverse_recursive(node):
            if node.next is None:
                return node

            next_node = _reverse_recursive(node.next)
            next_node.next = node
            return node

        # Call the recursive function and set the first node's next to None
        last_node = _reverse_recursive(head)
        head.next = None
        return last_node

class LinkedList: 
    def __init__(self, head) -> None:
        self.head = head

    def fromHead(head: ListNode):
        return 

    def insert(self, val):

        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            return 
        
        current = self.head
        while current.next: 
            current = current.next

        current.next = new_node

    def print(self):
        if self.head is None: 
            print("The linked list is empty!")
            return 
        
        current = self.head
        while current: 
            print(current.val)
            current = current.next

    def pop_front(self) -> ListNode:
        if self.head is None: 
            print("The list is empty")
            return None

        node = self.head
        self.head = self.head.next
        return node
    
    def pop(self) -> ListNode: 
        if self.head is None: 
            print("The list is empty")
            return None 
        
        current = self.head 
        while current.next: 
            current = current.next

        return current
    
    def delete(self, index):
        if self.head is None:
            print("The list is empty")
            return 
        
        current = self.head 
        position = 0

        if index == 0:
            self.pop_front()
            return
        
        while current.next is not None and position < index - 1: 
            position += 1
            current = current.next

        if current is None or current.next is None: 
            print("Index not present")
        else: 
            current.next = current.next.next

    def traverse(self):
        self.rec_traverse(self.head)

    def rec_traverse(self, node):
        if node is None:
            return 
        
        print(node.val)
        self.rec_traverse(node.next)

    def reverse(self):
        if self.head is None: 
            print("List is empty")
            return

        node = self.rec_reverse(self.head)
        node.next = None

    def rec_reverse(self, node) -> ListNode: 
        if node.next is None: 
            self.head = node
            return node

        next_node = self.rec_reverse(node.next)
        next_node.next = node
        return node
    
def copyRandomList(head):
        if head is None: 
            return None

        newHead = ListNode(head.val)
        newCurr = newHead
        curr = head.next

        while curr: 
            newNode = ListNode(curr.val)
            newCurr.next = newNode
            newCurr = newCurr.next
            curr = curr.next

        return newHead


# llist = LinkedList(ListNode(1))
# llist.insert(2)
# llist.insert(3)
# llist.insert(4)
# llist.insert(5)
# llist.insert(6)
# llist.reverse()
# llist.print()
# newllist = LinkedList(copyRandomList(llist.head))
# newllist.print()
