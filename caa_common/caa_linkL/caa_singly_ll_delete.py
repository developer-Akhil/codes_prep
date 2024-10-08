class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:
    def __init__(self):
      self.head = None

    def insert(self,newNode):
        if self.head is None:
           self.head = newNode

        else:
            lastNode = self.head

            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def deleteEnd(self):
        #head=>John->Ben->Mattew->None
        lastNode=self.head

        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next=None


    def printList(self):

        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next

firstNode=Node("John")
linkedList=LinkedList()
linkedList.insert(firstNode)
secondNode=Node("Ben")
linkedList.insert(secondNode)
thirdNode=Node("Mattew")
linkedList.insert(thirdNode)

linkedList.deleteEnd()
linkedList.printList()