class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        
        l1 = head
        countOfNodes, l2 = self.findMidNode(head)
        l2 = self.reverseList(l2)
        
        count = 0
        while count < countOfNodes//2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
            count+=1
        
        return True
        
    def findMidNode(self, head):
        slowPointer = head
        fastPointer = head
        
        count = 0
        
        while fastPointer.next and fastPointer.next.next is not None:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            count+=2
        if fastPointer.next is None:
            count+=1
            return count, slowPointer
        else:
            count+=2
            return count, slowPointer.next
        
    def reverseList(self, head):
        prevNode = None
        currentNode = head
        
        while currentNode is not None:
            tempNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            
            currentNode = tempNode
        
        return prevNode