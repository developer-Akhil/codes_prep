class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.start = None

    def deleteFirst(self):
        if self.start is None:
            print("Linked list is empty")
        else:
            temp = self.start
            self.start = self.start.next

    def insertLast(self, value):
        newNode = Node(value)
        if self.start is None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def viewList(self):

        if self.start is None:
            print("List is empty")
        else:
            temp = self.start
            while temp is not None:
                print(temp.data, end=' ')
                temp = temp.next

    def reverseList(self):

        prev = None

        while self.start:

            temp = self.start
            self.start = self.start.next
            temp.next = prev
            prev = temp
        return prev


mylist = LinkedList()
mylist.insertLast(10)
mylist.insertLast(20)
mylist.insertLast(30)
mylist.insertLast(40)
mylist.viewList()
print("\n")
reversList = mylist.reverseList()

# print(reversList.data)

while reversList:
    print(reversList.data,end=" ")
    reversList = reversList.next

# mylist.deleteFirst()

# mylist.viewList()
# input()
