from typing import Optional
from ListNode import ListNode

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    
    current = head 
    while current.next:
        current = current.next

    