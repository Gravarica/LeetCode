from ListNode import ListNode, LinkedList

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy 
    carry = 0
    while l1 or l2: 
        val1 = l1.val if l1 else 0 
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10 
        digit = total % 10

        curr.next = ListNode(digit)
        curr = curr.next

        if l1: 
            l1 = l1.next 
        if l2:
            l2 = l2.next

    if carry:
        curr.next = ListNode(carry)

    return dummy.next

list1 = LinkedList(ListNode(9))
list1.insert(9)
list1.insert(9)
list1.insert(9)
list1.insert(9)
list1.insert(9)
list1.insert(9)
list2 = LinkedList(ListNode(9))
list2.insert(9)
list2.insert(9)
list2.insert(9)
head = addTwoNumbers(list1.head, list2.head)
list1.print()