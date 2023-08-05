
# videos: https://www.youtube.com/watch?v=y_vt8_Zqu8U
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return
        currentNode =self.head
        while currentNode.next is not self.head:
            currentNode = currentNode.next
        currentNode.next = newNode
        newNode.next = self.head

    def printList(self):

        currentNode = self.head
        while True:
            print(currentNode.data)

            if currentNode.next is self.head:
                break
            currentNode=currentNode.next
        currentNode = currentNode.next
        print(currentNode.data)

nodeOne=Node('Jone')
nodeTwo=Node('Ben')
nodeThree=Node('Akhil')

linkList = LinkedList()
linkList.insert(nodeOne)
linkList.insert(nodeTwo)
linkList.insert(nodeThree)

linkList.printList()
