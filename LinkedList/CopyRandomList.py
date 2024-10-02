from ListNode import ListNode

def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: 
            return None

        dictionary = {}
        newHead = ListNode(head.val)
        newCurr = newHead
        dictionary[head] = newHead
        curr = head.next

        while curr: 
            newNode = ListNode(curr.val)
            dictionary[curr] = newNode
            newCurr.next = newNode
            newCurr = newCurr.next
            curr = curr.next

        curr = head
        while curr:
            if curr.random is not None: 
                dictionary[curr].random = dictionary[curr.random]
            curr = curr.next

        return newHead