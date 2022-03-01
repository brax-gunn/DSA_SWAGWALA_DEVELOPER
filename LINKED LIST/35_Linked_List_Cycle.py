class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slowPointer = fastPointer = head
        
        if head is None or head.next is None:
            return False
        
        while fastPointer.next and fastPointer.next.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next 
            
            if slowPointer == fastPointer:
                return True
        
        return False