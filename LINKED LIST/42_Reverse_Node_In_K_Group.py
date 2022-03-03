from collections import deque

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        myStack = deque()
        myQueue = deque()
        
        kLeft = k
        currentNode = head
        while currentNode:
            if kLeft <= 0:
                while len(myStack):
                    myQueue.append(myStack.pop())
                kLeft = k
                
            myStack.append(currentNode.val)
            kLeft -= 1
            currentNode = currentNode.next
        if kLeft <= 0:
            while len(myStack):
                myQueue.append(myStack.pop())
                
        
        currentNode = head
        while len(myQueue):
            currentNode.val = myQueue.popleft()
            currentNode = currentNode.next
        
        return head