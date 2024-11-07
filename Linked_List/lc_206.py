# vedio : https://www.youtube.com/watch?v=RhCGA4jlPmQ&list=PLzjoZGHG3J8vdUH75YPqmO7lbQl_M-xXo&index=2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
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
            print(currentNode.data, end=' ')
            currentNode = currentNode.next

    def reverseList(self, head) -> Node:

        prev = None

        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp

        return prev


from typing import Optional

# class Solution:


firstNode = Node(1)
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node(2)
linkedList.insert(secondNode)
thirdNode = Node(3)
linkedList.insert(thirdNode)
fourthNode = Node(4)
linkedList.insert(fourthNode)
fifthNode = Node(5)
linkedList.insert(fifthNode)
linkedList.printList()

rev = linkedList.reverseList(firstNode)

print("\n")
while rev:
    print(rev.data, end=' ')
    rev = rev.next

