# insert a node in beginning in linked list
# video : 1) https://www.youtube.com/watch?v=h29zxRMOXgA&list=PLzjoZGHG3J8vdUH75YPqmO7lbQl_M-xXo&index=3    (Theory)
#         2) https://www.youtube.com/watch?v=nH_nhfEZ7hc&list=PLzjoZGHG3J8vdUH75YPqmO7lbQl_M-xXo&index=4    (Practical)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkList():

    def __init__(self):
        self.head = None

    def insertHead(self,newNode):
        temporaryNode = self.head
        self.head=newNode
        newNode.next=temporaryNode

        del temporaryNode

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

    def printList(self):

        currentNode = self.head
        while True:

            if currentNode is None:
                break

            print(currentNode.data)
            currentNode=currentNode.next


firstNode=Node("John")
linkList=LinkList()
linkList.insert(firstNode)

secondNode=Node("Ben")
linkList.insert(secondNode)

thirdNode = Node("Matthew")
linkList.insertHead(thirdNode)
linkList.printList()



