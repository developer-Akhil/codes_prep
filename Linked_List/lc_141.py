""" write a function that determines if a singly linked list is circular and if it is, we are going to return the node where the cycle begins.
This solution is based off of Robert Floyd’s algorithm, first discovered in the 1970’s. """

""" Floyd’s cycle finding algorithm or Hare-Tortoise algorithm is a pointer algorithm that uses only two pointers, moving through the sequence
at different speeds. This algorithm is used to find a loop in a linked list. It uses two pointers one moving twice as fast as the other one.
The faster one is called the faster pointer and the other one is called the slow pointer. """

""" How Does Floyd’s Cycle Finding Algorithm Works? """

""" While traversing the linked list one of these things will occur """

""" 
1)  The Fast pointer may reach the end (NULL) this shows that there is no loop n the linked list.
2) The Fast pointer again catches the slow pointer at some time therefore a loop exists in the linked list.
"""

from typing import Optional

class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        # self.next = None


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        while fast and fast.next:

            slow = head.next
            fast = head.next.next
            print("klasjld")
            if slow == fast:
                print("kfdjsl")
                return True
        return False


firstNode = ListNode(1)
linkedList = Solution()

head = None
for i in reversed(range(5)):
    head = ListNode(i + 1, head)

# insert cycle
# head.next.next.next.next.next = head.next.next

if Solution().hasCycle(head):
    print('Cycle Found')
else:
    print('No Cycle Found')

# listNode=ListNode(1)
# listNode.val=2
# listNode.val=3
# listNode.val=4
# listNode.val=5
