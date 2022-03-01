class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummyNode = ListNode(-1)
        head = dummyNode
        
        while l1 or l2 is not None:
            if l1 is None:
                value = l2.val + carry
            elif l2 is None:
                value = l1.val + carry
            else:
                value = l1.val +  l2.val + carry
            
            if value >= 10:
                carry = value//10
                value = value - 10
            else:
                carry = 0
            
            newNode = ListNode(value)
            dummyNode.next = newNode
            dummyNode = newNode
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry != 0:
            newNode = ListNode(carry)
            dummyNode.next = newNode
            
        return head.next