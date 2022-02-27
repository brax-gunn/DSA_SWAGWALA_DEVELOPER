class Solution:
    def deleteNode(self, node):
        currentNode = node
        nextNode = node.next
        
        currentNode.val = nextNode.val
        currentNode.next = nextNode.next