#vedio : https://www.youtube.com/watch?v=RhCGA4jlPmQ&list=PLzjoZGHG3J8vdUH75YPqmO7lbQl_M-xXo&index=2
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
    def deleteAt(self,position):

        currentNode = self.head
        currentPosition=0
        while True:
            if currentPosition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
            previousNode=currentNode

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

linkedList.printList()

